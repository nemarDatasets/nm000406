import argparse
import re
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io

FLAT_STD = 100.0  # counts


def read_brainvision(vhdr: Path) -> tuple[list[str], np.ndarray]:
    header = vhdr.read_text(encoding="utf-8")
    assert "BinaryFormat=IEEE_FLOAT_32" in header and "DataOrientation=MULTIPLEXED" in header, vhdr
    channels = re.findall(r"^Ch\d+=([^,]*),[^,]*,([^,]*),", header, re.M)
    assert all(float(res) == 1 for _, res in channels), f"{vhdr}: resolution != 1: {channels}"
    data = np.fromfile(vhdr.with_suffix(".eeg"), dtype="<f4").reshape(-1, len(channels))
    return [name for name, _ in channels], data


def zenodo_channels(archive: zipfile.ZipFile, member: str) -> dict[str, np.ndarray]:
    with archive.open(member) as f:
        mat = scipy.io.loadmat(f, squeeze_me=True, struct_as_record=False)
    return {str(s.channel): np.asarray(s.data).ravel() for s in np.atleast_1d(mat["signal"])}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, help="nm000406 dataset root")
    parser.add_argument("--zenodo-zip", type=Path, help="data.zip of Zenodo record 7352058")
    args = parser.parse_args()
    archive = None if args.zenodo_zip is None else zipfile.ZipFile(args.zenodo_zip)

    rows = []
    for scans in sorted(args.root.glob("sub-*/sub-*_scans.tsv")):
        for rec in pd.read_csv(scans, sep="\t", dtype=str).itertuples():
            names, data = read_brainvision(scans.parent / rec.filename)
            assert names == ["Electrode1", "Electrode2", "Electrode3"], (rec.filename, names)
            source = None if archive is None else zenodo_channels(archive, rec.source_file)
            row = {"run": Path(rec.filename).name.removesuffix("_ieeg.vhdr"), "identical": 0}
            for j, name in enumerate(names):
                n = int((~np.isnan(data[:, j])).sum())
                x = data[:n, j]
                assert not np.isnan(x).any(), f"{rec.filename} {name}: NaN before the end of the channel"
                row[name] = x.astype(np.float64).std()
                if source is not None:
                    row["identical"] += np.array_equal(x, source[name].astype(np.float32))
            flat = row["Electrode1"] < FLAT_STD
            row["status"] = "bad" if flat else "good"
            row["status_description"] = f"near flat: std {row['Electrode1']:.1f} counts (< 100)" if flat else "n/a"
            rows.append(row)
    df = pd.DataFrame(rows)
    df["subject"] = df["run"].str.split("_").str[0]

    flat = df["status"] == "bad"
    others = pd.concat([df["Electrode2"], df["Electrode3"]])
    summary = [
        ("files", f"{len(df)}"),
        ("Electrode1 std < 100 counts (status bad)", f"{flat.sum()} files"),
        ("Electrode1 std, bad files", f"{df.loc[flat, 'Electrode1'].min():.1f}-{df.loc[flat, 'Electrode1'].max():.1f}"),
        ("Electrode1 std, other files", f"{df.loc[~flat, 'Electrode1'].min():.0f}-{df.loc[~flat, 'Electrode1'].max():.0f}"),
        ("Electrode2/3 std, all files", f"{others.min():.0f}-{others.max():.0f}"),
        ("subjects without a bad Electrode1", ", ".join(sorted(set(df["subject"]) - set(df.loc[flat, "subject"])))),
    ]
    if archive is not None:
        summary.append(("channels identical to the Zenodo .mat (int16 -> float32)", f"{df['identical'].sum()} of {3 * len(df)}"))
    print("| quantity | value |\n|---|---|")
    for key, value in summary:
        print(f"| {key} | {value} |")

    print("\n| subject | files | Electrode1 bad |\n|---|---:|---:|")
    for subject, group in df.groupby("subject"):
        print(f"| {subject} | {len(group)} | {(group['status'] == 'bad').sum()} |")

    print("\n| run | Electrode1 std | Electrode2 std | Electrode3 std | Electrode1 status | status_description |")
    print("|---|---:|---:|---:|---|---|")
    for r in df.itertuples():
        print(f"| {r.run} | {r.Electrode1:.1f} | {r.Electrode2:.1f} | {r.Electrode3:.1f} | {r.status} | {r.status_description} |")


if __name__ == "__main__":
    main()
