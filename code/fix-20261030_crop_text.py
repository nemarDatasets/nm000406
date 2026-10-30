"""nm000406, Oct 2026 (external review, J. Gadonneix issue #4): sidecar/README changes that go with cropping the 226
NaN-padded recordings to their shortest channel (data files written by crop406.py, manifest in
code/fix-20261030_crop_manifest.tsv). Deterministic; run from the dataset root: python fix406_crop_text.py
  - <run>_ieeg.json: RecordingDuration = new samples / SamplingFrequency; RecordingDescription states the crop.
  - sub-XX_scans.tsv: n_samples = samples in the cropped file; scans.json description updated.
  - the 226 events.tsv (only BAD_nan rows, which marked the NaN padding) are removed, and task-mer_events.json with
    them (no other events.tsv exists in this dataset).
  - README: Layout bullet and the NaN section rewritten.
"""
import csv, glob, json, os, re, subprocess

man = list(csv.DictReader(open("code/fix-20261030_crop_manifest.tsv"), delimiter="\t"))
assert len(man) == 226
OLD_DESC = ("Channels differ in length; shorter channels are NaN after their last sample (alignment of channels of "
            "unequal length is not documented; all are written from their first sample).")
nj = ns = ne = 0
for r in man:
    b = r["recording"][:-len("_ieeg.eeg")]
    L = int(r["n_times_new"]); n_old = int(r["n_times_old"])
    p = b + "_ieeg.json"
    d = json.load(open(p, encoding="utf-8"))
    assert OLD_DESC in d["RecordingDescription"], p
    d["RecordingDescription"] = d["RecordingDescription"].replace(
        OLD_DESC,
        f"Channels differ in length in the release. Since Oct 2026 this file is cropped to the shortest channel "
        f"({L} samples; {n_old - L} samples of the longer channels after that point are left out; they remain in the "
        f"release .mat in sourcedata). All channels are written from their first sample (alignment of channels of "
        f"unequal length is not documented).")
    fs = float(d["SamplingFrequency"])
    assert abs(d["RecordingDuration"] - n_old / fs) < 1e-3, (p, d["RecordingDuration"], n_old / fs)
    d["RecordingDuration"] = L / fs
    txt = json.dumps(d, indent=2, ensure_ascii=False) + "\n"
    open(p, "w", encoding="utf-8").write(txt)
    nj += 1
    ev = b + "_events.tsv"
    rows = [l.rstrip("\n").split("\t") for l in open(ev, encoding="utf-8")]
    assert rows[0][:3] == ["onset", "duration", "trial_type"] and all(x[2] == "BAD_nan" for x in rows[1:]), ev
    assert len(rows) == 2 and int(rows[1][3]) == L, (ev, rows)
    subprocess.run(["git", "rm", "-q", ev], check=True)
    ne += 1
# scans.tsv
new = {r["recording"][:-len(".eeg")] + ".vhdr": r for r in man}
for sc in sorted(glob.glob("sub-*/sub-*_scans.tsv")):
    sub = os.path.dirname(sc)
    rows = list(csv.reader(open(sc, encoding="utf-8"), delimiter="\t"))
    h = rows[0]; i_f = h.index("filename"); i_n = h.index("n_samples")
    ch = False
    for row in rows[1:]:
        key = f"{sub}/{row[i_f]}"
        if key in new:
            assert int(row[i_n]) == int(new[key]["n_times_old"]), (key, row[i_n])
            row[i_n] = new[key]["n_times_new"]; ns += 1; ch = True
    if ch:
        with open(sc, "w", encoding="utf-8", newline="") as f:
            csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
for sj in sorted(glob.glob("sub-*/sub-*_scans.json")):
    d = json.load(open(sj, encoding="utf-8"))
    assert d["n_samples"]["Description"] == "Samples in the BrainVision file (= longest channel)", sj
    d["n_samples"]["Description"] = ("Samples in the BrainVision file (= the shortest channel: since Oct 2026 the "
                                     "files whose channels differ in length are cropped to the shortest channel; "
                                     "per-channel source lengths are in channels.tsv, source_n_samples)")
    open(sj, "w", encoding="utf-8").write(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
assert not glob.glob("sub-*/**/*_events.tsv", recursive=True)
subprocess.run(["git", "rm", "-q", "task-mer_events.json"], check=True)
# README
t = open("README.md", encoding="utf-8").read()
old_layout = ("- In 226 of the 830 files the three channels have different lengths (differences are whole 752-sample blocks). The\n"
              "  release does not document how channels of unequal length line up. Every channel is written from its first sample, and\n"
              "  shorter channels are NaN after their last sample. `channels.tsv` gives each channel's source length\n"
              "  (`source_n_samples`), and the sidecar's `RecordingDescription` repeats the lengths.\n")
new_layout = ("- In 226 of the 830 files the three channels have different lengths (differences are whole 752-sample blocks). The\n"
              "  release does not document how channels of unequal length line up. Every channel is written from its first sample.\n"
              "  Since Oct 2026 these 226 files are cropped to their shortest channel (see 'Cropped recordings' below), so no file\n"
              "  holds NaN samples. `channels.tsv` gives each channel's source length (`source_n_samples`), and the sidecar's\n"
              "  `RecordingDescription` repeats the lengths.\n")
assert t.count(old_layout) == 1
t = t.replace(old_layout, new_layout)
i0 = t.index("## NaN samples in the signal files (checked 19 Oct 2026)")
i1 = t.find("\n## ", i0 + 5)
tot_removed = sum(int(r["removed_samples"]) for r in man)
mx = max(int(r["removed_samples"]) for r in man)
sec = f"""## Cropped recordings (Oct 2026)

In 226 recordings the release channels have different lengths. These files used to keep every channel at its full
length and pad the shorter channels with NaN (not-a-number) samples at the end, marked by `BAD_nan` rows in
`events.tsv` (Oct 2026). Following an external review (J. Gadonneix, Oct 2026, issue #4 of this repository), each of
these 226 files is now cropped to its shortest channel: the file keeps the first N samples of every channel, where N is
the length of the shortest channel, so no NaN sample remains. The kept samples are unchanged bit for bit (the new
`.eeg` is a byte prefix of the old one; every file was checked by reading it with MNE). The samples of the longer
channels after that point are left out of the BIDS files: {mx} samples per file at most, {tot_removed} samples in
total. They remain in the release `.mat` files in `sourcedata/`, and each channel's source length is in
`channels.tsv` (`source_n_samples`).

The 226 `events.tsv` files that held only the `BAD_nan` rows, and `task-mer_events.json`, are removed. `RecordingDuration`
in the sidecars and `n_samples` in `scans.tsv` give the cropped lengths. Per recording (old and new length, samples left
out, channels involved, old annex key, new size and SHA-256): `code/fix-20261030_crop_manifest.tsv`; code:
`code/fix-20261030_crop406.py` (data) and `code/fix-20261030_crop_text.py` (sidecars). `code/fix-20261019_nan_spans.tsv`
is the NaN scan of the uncropped files (Oct 2026); `code/fix-20261018_nan_scan.json` an earlier, partial scan.
"""
t = t[:i0] + sec + (t[i1:] if i1 != -1 else "")
open("README.md", "w", encoding="utf-8").write(t)
print(f"ieeg.json {nj}, scans rows {ns}, events.tsv removed {ne}")
