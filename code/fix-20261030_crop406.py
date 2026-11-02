"""nm000406: crop the 226 recordings whose shorter channels are NaN-padded to the length of their shortest channel.

Input: code/fix-20261019_nan_spans.tsv of the nm000406 clone (one BAD_nan row per recording: start_sample = first NaN
sample = length of the shortest channel, n_times = current length). For each recording:
  1. fetch the .vhdr/.vmrk/.eeg by annex key from the NEMAR S3 bucket (size + sha256 checked, s3fetch.py);
  2. read the .eeg as IEEE float32, MULTIPLEXED, 3 channels (as the .vhdr states; checked);
  3. check: n_times as in the table; every sample before start_sample finite in every channel; from start_sample on,
     the channels listed in the table are NaN to the end and the others are finite;
  4. write the first start_sample samples (a byte prefix of the multiplexed file, so the kept samples are unchanged
     bit for bit) to <out>/<rel>.eeg, and check it with MNE (n_times, no NaN, equal to the original prefix).
Writes <out>/manifest.tsv (old/new size, sha256, removed samples). Nothing is written to the repository.
Usage: crop406.py <repo> <out>
"""
import csv, hashlib, os, re, shutil, sys
import numpy as np
import mne

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib; s3fetch = importlib.import_module("fix-20261030_s3fetch")

mne.set_log_level("ERROR")
repo, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
rows = list(csv.DictReader(open(f"{repo}/code/fix-20261019_nan_spans.tsv"), delimiter="\t"))
rows = [r for r in rows if r["kind"] == "BAD_nan"]
assert len(rows) == 226, len(rows)
man = open(f"{out}/manifest.tsv", "w")
man.write("recording\tn_times_old\tn_times_new\tremoved_samples\tremoved_s\tnan_channels\tchannel_lengths\told_key\told_bytes\tnew_bytes\tnew_sha256\tprefix_equal\tmne_ok\n")
tot_old = tot_new = 0
for r in rows:
    vh = r["recording"]
    b = vh[:-5]
    loc = s3fetch.materialize(repo, [b + ".vhdr", b + ".vmrk", b + ".eeg"], "/work/d406", ds="nm000406")
    hdr = open(loc[b + ".vhdr"], encoding="utf-8").read()
    assert "DataOrientation=MULTIPLEXED" in hdr and "BinaryFormat=IEEE_FLOAT_32" in hdr
    nch = int(re.search(r"NumberOfChannels=(\d+)", hdr).group(1))
    names = re.findall(r"^Ch\d+=([^,]+),", hdr, re.M)
    assert len(names) == nch
    a = np.fromfile(loc[b + ".eeg"], dtype="<f4")
    assert a.size % nch == 0
    a = a.reshape(-1, nch)
    n_old = a.shape[0]
    L = int(r["start_sample"])
    assert n_old == int(r["n_times"]), (vh, n_old, r["n_times"])
    assert int(r["stop_sample"]) == n_old and int(r["n_samples"]) == n_old - L
    nanch = r["channels"].split(",")
    assert np.isfinite(a[:L]).all(), vh
    lens = []
    for i, c in enumerate(names):
        fin = np.isfinite(a[:, i])
        li = int(fin.sum())  # channel length: finite samples, all at the start, NaN padding after
        assert fin[:li].all() and not fin[li:].any(), (vh, c, "NaN not a trailing pad")
        assert (li < n_old) == (c in nanch), (vh, c, li, n_old)
        lens.append(li)
    assert min(lens) == L, (vh, lens, L)
    raw_bytes = open(loc[b + ".eeg"], "rb").read()
    newb = raw_bytes[: L * nch * 4]
    dst = f"{out}/{b}.eeg"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "wb").write(newb)
    sha = hashlib.sha256(newb).hexdigest()
    # MNE check on the cropped file with the unchanged header/marker files
    chk = f"/work/chk/{os.path.basename(b)}"
    os.makedirs(os.path.dirname(chk), exist_ok=True)
    shutil.copyfile(loc[b + ".vhdr"], chk + ".vhdr")
    shutil.copyfile(loc[b + ".vmrk"], chk + ".vmrk")
    shutil.copyfile(dst, chk + ".eeg")
    raw = mne.io.read_raw_brainvision(chk + ".vhdr", preload=True)
    d = raw.get_data()
    ref = a[:L].astype(np.float64)
    nz = ref != 0
    scale = float(np.median(d.T[nz] / ref[nz])) if nz.any() else 1.0  # MNE unit scaling of 'unscaled' channels
    mne_ok = raw.n_times == L and np.isfinite(d).all() and np.allclose(d.T, ref * scale, rtol=1e-6, atol=0)
    prefix_equal = np.array_equal(np.frombuffer(newb, dtype="<f4").reshape(-1, nch), a[:L])
    assert mne_ok and prefix_equal, vh
    old_key = os.path.basename(open(os.path.join(repo, b + ".eeg"), "rb").read(300).decode().strip())
    man.write(f"{b}.eeg\t{n_old}\t{L}\t{n_old-L}\t{(n_old-L)/raw.info['sfreq']:.6f}\t{r['channels']}\t{",".join(map(str, lens))}\t{old_key}\t{len(raw_bytes)}\t{len(newb)}\t{sha}\t{prefix_equal}\t{mne_ok}\n")
    man.flush()
    tot_old += len(raw_bytes); tot_new += len(newb)
    for p in list(loc.values()) + [chk + ".vhdr", chk + ".vmrk", chk + ".eeg"]:
        os.remove(p)
    print(b, n_old, L, flush=True)
man.close()
print("TOTAL old_bytes", tot_old, "new_bytes", tot_new, flush=True)
open(f"{out}/DONE", "w").write(f"{tot_old} {tot_new}\n")
