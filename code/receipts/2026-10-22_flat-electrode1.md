# Mark near-flat Electrode1 as bad

**Claim**: Electrode1 has a std below 100 counts in 692 of 830 files (4.6-15.9 counts, all patients except P4 and P8) and
is marked `bad` there, with the std in `status_description` (PR nemarDatasets/nm000406#3, head
`e44e1035028407c0e24cfd46e37888f5a601fc49`).

**Source**
- NEMAR nm000406 at `origin/main` `dc1b430c6bc1a077ffa32077d12ae7f1a29f1c7d`: all 830 recordings
  `sub-*/ieeg/*_task-mer_*_ieeg.{vhdr,eeg}` and the 14 `sub-*_scans.tsv`. Identification: sha256 of each annexed file read
  (830 `.vhdr`, 830 `.eeg`) equals its SHA256E git-annex key at that commit; the 14 `scans.tsv` equal the git blobs.
- Upstream: Zenodo record 7352058 (doi:10.5281/zenodo.7352058), `data.zip`, 7360966582 bytes, md5
  `ca79e26263a3507a6edec3346eae3c65` as listed by the record; each run's source `.mat` is the `source_file` of `scans.tsv`
  (also in `sourcedata/b3w2_provenance_c-mer.json`).

**Method**
- Reader: numpy on the BrainVision binary (IEEE_FLOAT_32, multiplexed, resolution 1: the release's int16 values, no
  scaling, units n/a). Each channel is taken up to its last non-NaN sample (shorter channels are NaN-padded; checked: no
  NaN inside).
- Per channel: std of those samples (numpy, ddof 0, float64), in counts.
- Electrode1 is `bad` if its std < 100 counts; `status_description` = `near flat: std <std, 1 decimal> counts (< 100)`.
- Upstream check: the release `.mat` (`scipy.io.loadmat`, struct `signal`: `channel`, int16 `data`) of each run read from
  `data.zip`; a channel is identical if the BIDS samples equal the int16 values cast to float32, same length.

**Result**

| quantity | value |
|---|---|
| files | 830 |
| Electrode1 std < 100 counts (status bad) | 692 files |
| Electrode1 std, bad files | 4.6-15.9 |
| Electrode1 std, other files | 216-7184 |
| Electrode2/3 std, all files | 224-11102 |
| subjects without a bad Electrode1 | sub-04, sub-08 |
| channels identical to the Zenodo .mat (int16 -> float32) | 2490 of 2490 |

| subject | files | Electrode1 bad |
|---|---:|---:|
| sub-01 | 24 | 24 |
| sub-02 | 66 | 66 |
| sub-03 | 79 | 79 |
| sub-04 | 62 | 0 |
| sub-05 | 41 | 41 |
| sub-06 | 40 | 40 |
| sub-07 | 30 | 30 |
| sub-08 | 76 | 0 |
| sub-09 | 79 | 79 |
| sub-10 | 92 | 92 |
| sub-11 | 37 | 37 |
| sub-12 | 83 | 83 |
| sub-13 | 86 | 86 |
| sub-14 | 35 | 35 |

<details><summary>Per run (830 rows)</summary>

| run | Electrode1 std | Electrode2 std | Electrode3 std | Electrode1 status | status_description |
|---|---:|---:|---:|---|---|
| sub-01_task-mer_acq-left_run-01 | 9.2 | 355.8 | 365.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-02 | 9.2 | 290.2 | 402.4 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-03 | 9.2 | 291.7 | 401.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-04 | 9.2 | 300.7 | 399.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-05 | 9.2 | 328.8 | 452.0 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-06 | 9.2 | 420.8 | 479.7 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-07 | 9.2 | 346.7 | 578.3 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-08 | 9.2 | 419.9 | 419.4 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-09 | 9.2 | 520.9 | 399.1 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-10 | 9.2 | 440.3 | 506.7 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-11 | 9.2 | 377.5 | 545.3 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-12 | 9.2 | 393.8 | 393.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-13 | 9.2 | 391.9 | 457.0 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-14 | 9.2 | 334.1 | 592.3 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-15 | 9.1 | 369.4 | 450.8 | bad | near flat: std 9.1 counts (< 100) |
| sub-01_task-mer_acq-left_run-16 | 11.0 | 430.8 | 468.7 | bad | near flat: std 11.0 counts (< 100) |
| sub-01_task-mer_acq-left_run-17 | 12.9 | 445.7 | 470.3 | bad | near flat: std 12.9 counts (< 100) |
| sub-01_task-mer_acq-left_run-18 | 9.2 | 545.8 | 454.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-19 | 9.2 | 626.4 | 448.4 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-20 | 9.2 | 359.9 | 398.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-21 | 9.2 | 332.2 | 433.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-22 | 9.2 | 499.9 | 474.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-23 | 9.2 | 303.2 | 339.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-01_task-mer_acq-left_run-24 | 9.2 | 304.7 | 419.0 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-01 | 11.2 | 5536.0 | 5938.6 | bad | near flat: std 11.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-02 | 9.2 | 288.1 | 305.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-03 | 9.2 | 304.6 | 320.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-04 | 9.2 | 327.6 | 310.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-05 | 9.2 | 317.5 | 316.1 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-06 | 9.2 | 630.1 | 316.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-07 | 9.2 | 614.7 | 347.1 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-08 | 9.2 | 368.1 | 531.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-09 | 9.2 | 420.7 | 527.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-10 | 9.2 | 382.1 | 558.3 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-11 | 9.2 | 394.7 | 653.0 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-12 | 9.2 | 519.7 | 727.3 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-13 | 9.2 | 552.9 | 521.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-14 | 9.2 | 633.9 | 619.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-15 | 9.2 | 534.6 | 659.4 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-16 | 9.2 | 658.2 | 779.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-17 | 9.2 | 929.2 | 763.1 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-18 | 9.2 | 556.8 | 665.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-19 | 9.2 | 474.2 | 514.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-20 | 9.2 | 576.8 | 781.0 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-21 | 9.2 | 1110.3 | 668.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-22 | 9.2 | 572.9 | 478.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-23 | 9.2 | 665.7 | 423.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-24 | 9.2 | 560.0 | 363.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-25 | 9.2 | 606.8 | 346.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-26 | 9.2 | 484.4 | 355.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-27 | 9.2 | 516.2 | 339.4 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-28 | 9.2 | 487.9 | 334.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-29 | 9.2 | 820.7 | 341.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-30 | 9.2 | 533.5 | 321.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-left_run-31 | 9.3 | 446.4 | 310.2 | bad | near flat: std 9.3 counts (< 100) |
| sub-02_task-mer_acq-left_run-32 | 9.2 | 470.5 | 312.0 | bad | near flat: std 9.2 counts (< 100) |
| sub-02_task-mer_acq-right_run-01 | 12.2 | 3000.5 | 3996.3 | bad | near flat: std 12.2 counts (< 100) |
| sub-02_task-mer_acq-right_run-02 | 9.1 | 506.3 | 296.7 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-03 | 9.1 | 423.4 | 295.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-04 | 9.1 | 323.7 | 294.1 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-05 | 9.1 | 337.5 | 306.8 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-06 | 9.1 | 367.8 | 301.6 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-07 | 9.1 | 368.6 | 312.8 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-08 | 9.1 | 436.5 | 326.1 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-09 | 9.1 | 471.0 | 276.5 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-10 | 9.1 | 565.3 | 277.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-11 | 9.1 | 489.8 | 343.7 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-12 | 9.1 | 388.3 | 582.9 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-13 | 9.1 | 299.7 | 775.8 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-14 | 9.1 | 419.9 | 509.9 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-15 | 9.1 | 361.7 | 871.6 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-16 | 9.1 | 387.9 | 493.4 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-17 | 9.1 | 530.6 | 597.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-18 | 9.1 | 464.8 | 401.2 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-19 | 9.1 | 961.4 | 459.3 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-20 | 9.1 | 495.1 | 365.8 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-21 | 9.1 | 323.9 | 465.5 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-22 | 9.1 | 337.7 | 305.2 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-23 | 9.1 | 518.4 | 303.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-24 | 9.1 | 854.9 | 312.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-25 | 9.1 | 494.1 | 318.5 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-26 | 9.1 | 707.3 | 330.5 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-27 | 9.1 | 786.8 | 338.6 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-28 | 9.1 | 577.8 | 374.5 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-29 | 9.1 | 527.3 | 336.2 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-30 | 9.1 | 490.9 | 320.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-31 | 9.1 | 343.7 | 299.5 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-32 | 9.1 | 396.1 | 288.8 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-33 | 9.1 | 292.0 | 288.7 | bad | near flat: std 9.1 counts (< 100) |
| sub-02_task-mer_acq-right_run-34 | 9.1 | 272.2 | 325.1 | bad | near flat: std 9.1 counts (< 100) |
| sub-03_task-mer_acq-left_run-01 | 5.2 | 455.1 | 366.0 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-02 | 5.4 | 2852.4 | 2712.3 | bad | near flat: std 5.4 counts (< 100) |
| sub-03_task-mer_acq-left_run-03 | 5.2 | 472.3 | 313.7 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-04 | 5.2 | 393.1 | 311.9 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-05 | 5.2 | 349.1 | 297.5 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-06 | 5.2 | 373.2 | 301.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-07 | 5.2 | 390.4 | 311.1 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-08 | 5.2 | 456.8 | 308.1 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-09 | 5.2 | 458.6 | 293.9 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-10 | 5.2 | 452.3 | 313.6 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-11 | 5.2 | 574.2 | 322.0 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-12 | 5.2 | 508.4 | 331.0 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-13 | 5.2 | 480.6 | 335.0 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-14 | 5.2 | 527.9 | 342.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-15 | 5.2 | 456.8 | 353.4 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-16 | 5.2 | 437.3 | 361.8 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-17 | 5.2 | 431.4 | 359.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-18 | 5.2 | 628.9 | 399.4 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-19 | 5.2 | 536.2 | 360.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-20 | 5.2 | 516.4 | 422.3 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-21 | 5.2 | 552.5 | 379.6 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-22 | 5.2 | 525.5 | 390.8 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-23 | 5.2 | 586.5 | 370.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-24 | 5.2 | 563.4 | 444.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-25 | 5.2 | 676.3 | 384.5 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-26 | 5.2 | 491.6 | 334.7 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-27 | 5.2 | 467.5 | 341.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-28 | 5.2 | 471.2 | 341.3 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-29 | 5.2 | 471.5 | 345.3 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-30 | 5.2 | 448.7 | 376.1 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-31 | 5.2 | 397.7 | 362.5 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-32 | 5.2 | 639.2 | 355.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-33 | 5.2 | 437.4 | 476.4 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-34 | 5.2 | 473.7 | 345.1 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-35 | 5.2 | 651.6 | 342.1 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-36 | 5.1 | 387.7 | 346.4 | bad | near flat: std 5.1 counts (< 100) |
| sub-03_task-mer_acq-left_run-37 | 5.2 | 373.6 | 339.6 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-38 | 5.4 | 3719.4 | 3834.6 | bad | near flat: std 5.4 counts (< 100) |
| sub-03_task-mer_acq-left_run-39 | 5.2 | 524.7 | 371.5 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-left_run-40 | 5.2 | 561.2 | 381.6 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-01 | 5.3 | 520.7 | 1290.3 | bad | near flat: std 5.3 counts (< 100) |
| sub-03_task-mer_acq-right_run-02 | 5.2 | 305.0 | 324.3 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-03 | 5.2 | 397.3 | 402.3 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-04 | 5.2 | 462.7 | 758.1 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-05 | 5.2 | 603.2 | 839.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-06 | 5.2 | 763.5 | 549.1 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-07 | 5.2 | 380.7 | 617.7 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-08 | 5.2 | 504.5 | 409.6 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-09 | 5.2 | 346.2 | 681.9 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-10 | 5.2 | 508.6 | 390.4 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-11 | 5.2 | 425.0 | 914.9 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-12 | 5.2 | 443.6 | 459.6 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-13 | 5.2 | 540.0 | 933.6 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-14 | 5.2 | 422.7 | 674.6 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-15 | 6.6 | 3260.3 | 2395.9 | bad | near flat: std 6.6 counts (< 100) |
| sub-03_task-mer_acq-right_run-16 | 5.8 | 3573.0 | 1536.7 | bad | near flat: std 5.8 counts (< 100) |
| sub-03_task-mer_acq-right_run-17 | 5.2 | 632.9 | 624.4 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-18 | 5.2 | 465.9 | 434.4 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-19 | 5.2 | 464.2 | 435.7 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-20 | 5.2 | 464.4 | 444.0 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-21 | 5.2 | 495.8 | 448.3 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-22 | 5.2 | 477.0 | 424.0 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-23 | 5.2 | 581.9 | 429.3 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-24 | 5.2 | 812.9 | 400.8 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-25 | 5.2 | 404.2 | 384.5 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-26 | 5.2 | 453.8 | 388.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-27 | 5.2 | 670.1 | 400.1 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-28 | 5.2 | 477.0 | 409.8 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-29 | 5.2 | 484.6 | 409.5 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-30 | 5.2 | 448.9 | 395.4 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-31 | 5.2 | 569.9 | 387.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-32 | 5.2 | 435.5 | 381.6 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-33 | 5.2 | 453.7 | 410.5 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-34 | 5.2 | 476.3 | 394.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-35 | 5.2 | 480.9 | 438.1 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-36 | 5.2 | 374.7 | 445.4 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-37 | 5.2 | 355.4 | 382.0 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-38 | 5.2 | 358.7 | 377.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-03_task-mer_acq-right_run-39 | 5.2 | 543.6 | 465.2 | bad | near flat: std 5.2 counts (< 100) |
| sub-04_task-mer_acq-left_run-01 | 237.0 | 4258.2 | 4370.1 | good | n/a |
| sub-04_task-mer_acq-left_run-02 | 217.4 | 535.1 | 464.6 | good | n/a |
| sub-04_task-mer_acq-left_run-03 | 217.7 | 511.5 | 450.1 | good | n/a |
| sub-04_task-mer_acq-left_run-04 | 217.4 | 812.5 | 485.5 | good | n/a |
| sub-04_task-mer_acq-left_run-05 | 217.1 | 469.0 | 492.4 | good | n/a |
| sub-04_task-mer_acq-left_run-06 | 217.3 | 456.2 | 542.6 | good | n/a |
| sub-04_task-mer_acq-left_run-07 | 217.2 | 513.4 | 514.5 | good | n/a |
| sub-04_task-mer_acq-left_run-08 | 217.5 | 452.5 | 507.1 | good | n/a |
| sub-04_task-mer_acq-left_run-09 | 217.5 | 571.7 | 512.5 | good | n/a |
| sub-04_task-mer_acq-left_run-10 | 216.8 | 512.8 | 496.4 | good | n/a |
| sub-04_task-mer_acq-left_run-11 | 216.9 | 620.1 | 458.2 | good | n/a |
| sub-04_task-mer_acq-left_run-12 | 217.6 | 526.9 | 453.7 | good | n/a |
| sub-04_task-mer_acq-left_run-13 | 217.1 | 618.2 | 454.5 | good | n/a |
| sub-04_task-mer_acq-left_run-14 | 217.3 | 738.2 | 442.5 | good | n/a |
| sub-04_task-mer_acq-left_run-15 | 217.3 | 611.7 | 440.2 | good | n/a |
| sub-04_task-mer_acq-left_run-16 | 216.9 | 725.3 | 468.2 | good | n/a |
| sub-04_task-mer_acq-left_run-17 | 217.5 | 632.3 | 455.2 | good | n/a |
| sub-04_task-mer_acq-left_run-18 | 217.3 | 1525.6 | 464.4 | good | n/a |
| sub-04_task-mer_acq-left_run-19 | 217.4 | 603.1 | 458.3 | good | n/a |
| sub-04_task-mer_acq-left_run-20 | 217.3 | 681.0 | 453.5 | good | n/a |
| sub-04_task-mer_acq-left_run-21 | 217.1 | 852.6 | 452.9 | good | n/a |
| sub-04_task-mer_acq-left_run-22 | 217.1 | 594.5 | 462.1 | good | n/a |
| sub-04_task-mer_acq-left_run-23 | 217.2 | 805.8 | 455.9 | good | n/a |
| sub-04_task-mer_acq-left_run-24 | 217.0 | 683.0 | 458.0 | good | n/a |
| sub-04_task-mer_acq-left_run-25 | 217.1 | 735.3 | 441.6 | good | n/a |
| sub-04_task-mer_acq-left_run-26 | 216.9 | 472.5 | 441.5 | good | n/a |
| sub-04_task-mer_acq-left_run-27 | 217.1 | 697.2 | 433.0 | good | n/a |
| sub-04_task-mer_acq-left_run-28 | 217.0 | 424.0 | 444.8 | good | n/a |
| sub-04_task-mer_acq-left_run-29 | 217.2 | 379.2 | 431.8 | good | n/a |
| sub-04_task-mer_acq-left_run-30 | 216.9 | 365.3 | 403.1 | good | n/a |
| sub-04_task-mer_acq-left_run-31 | 216.7 | 432.9 | 422.2 | good | n/a |
| sub-04_task-mer_acq-left_run-32 | 216.3 | 341.5 | 436.2 | good | n/a |
| sub-04_task-mer_acq-right_run-01 | 230.0 | 3678.3 | 240.0 | good | n/a |
| sub-04_task-mer_acq-right_run-02 | 218.7 | 836.6 | 224.1 | good | n/a |
| sub-04_task-mer_acq-right_run-03 | 219.1 | 506.3 | 224.3 | good | n/a |
| sub-04_task-mer_acq-right_run-04 | 219.4 | 453.6 | 224.9 | good | n/a |
| sub-04_task-mer_acq-right_run-05 | 218.8 | 562.7 | 224.1 | good | n/a |
| sub-04_task-mer_acq-right_run-06 | 219.3 | 481.0 | 223.5 | good | n/a |
| sub-04_task-mer_acq-right_run-07 | 219.1 | 465.6 | 224.7 | good | n/a |
| sub-04_task-mer_acq-right_run-08 | 219.1 | 719.1 | 224.5 | good | n/a |
| sub-04_task-mer_acq-right_run-09 | 218.8 | 864.5 | 224.4 | good | n/a |
| sub-04_task-mer_acq-right_run-10 | 218.8 | 529.5 | 223.7 | good | n/a |
| sub-04_task-mer_acq-right_run-11 | 218.9 | 679.8 | 224.6 | good | n/a |
| sub-04_task-mer_acq-right_run-12 | 219.1 | 663.8 | 224.4 | good | n/a |
| sub-04_task-mer_acq-right_run-13 | 219.5 | 620.6 | 224.5 | good | n/a |
| sub-04_task-mer_acq-right_run-14 | 219.1 | 611.8 | 224.6 | good | n/a |
| sub-04_task-mer_acq-right_run-15 | 219.4 | 584.9 | 224.3 | good | n/a |
| sub-04_task-mer_acq-right_run-16 | 219.1 | 495.5 | 224.5 | good | n/a |
| sub-04_task-mer_acq-right_run-17 | 220.0 | 416.5 | 225.5 | good | n/a |
| sub-04_task-mer_acq-right_run-18 | 218.7 | 436.4 | 224.5 | good | n/a |
| sub-04_task-mer_acq-right_run-19 | 219.2 | 450.0 | 224.1 | good | n/a |
| sub-04_task-mer_acq-right_run-20 | 220.0 | 408.3 | 224.9 | good | n/a |
| sub-04_task-mer_acq-right_run-21 | 220.3 | 534.8 | 225.5 | good | n/a |
| sub-04_task-mer_acq-right_run-22 | 220.7 | 371.7 | 225.7 | good | n/a |
| sub-04_task-mer_acq-right_run-23 | 221.0 | 362.1 | 225.3 | good | n/a |
| sub-04_task-mer_acq-right_run-24 | 220.6 | 348.1 | 226.2 | good | n/a |
| sub-04_task-mer_acq-right_run-25 | 220.2 | 368.7 | 225.3 | good | n/a |
| sub-04_task-mer_acq-right_run-26 | 219.7 | 410.5 | 225.4 | good | n/a |
| sub-04_task-mer_acq-right_run-27 | 219.6 | 324.1 | 225.2 | good | n/a |
| sub-04_task-mer_acq-right_run-28 | 220.3 | 324.3 | 225.1 | good | n/a |
| sub-04_task-mer_acq-right_run-29 | 220.0 | 346.8 | 225.4 | good | n/a |
| sub-04_task-mer_acq-right_run-30 | 220.9 | 414.1 | 226.2 | good | n/a |
| sub-05_task-mer_acq-left_run-01 | 10.7 | 7227.7 | 4520.3 | bad | near flat: std 10.7 counts (< 100) |
| sub-05_task-mer_acq-left_run-02 | 9.2 | 680.9 | 401.7 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-03 | 9.2 | 617.4 | 389.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-04 | 9.2 | 435.1 | 415.4 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-05 | 9.2 | 359.1 | 434.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-06 | 9.2 | 484.6 | 551.0 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-07 | 9.2 | 429.4 | 512.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-08 | 9.2 | 459.3 | 652.1 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-09 | 9.2 | 377.2 | 620.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-10 | 9.2 | 745.3 | 911.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-11 | 9.2 | 582.2 | 629.0 | bad | near flat: std 9.2 counts (< 100) |
| sub-05_task-mer_acq-left_run-12 | 9.3 | 813.2 | 459.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-13 | 9.3 | 621.6 | 605.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-14 | 9.3 | 814.9 | 390.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-15 | 9.3 | 566.1 | 392.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-16 | 9.3 | 678.9 | 349.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-17 | 9.3 | 447.2 | 412.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-18 | 9.3 | 570.7 | 369.2 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-19 | 9.3 | 522.3 | 387.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-20 | 9.3 | 446.9 | 382.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-21 | 9.3 | 535.5 | 371.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-22 | 9.3 | 530.4 | 400.2 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-23 | 9.3 | 399.5 | 405.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-24 | 9.3 | 405.5 | 381.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-25 | 9.3 | 402.8 | 378.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-26 | 9.3 | 615.9 | 362.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-27 | 9.3 | 486.0 | 369.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-28 | 9.3 | 363.4 | 349.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-29 | 9.3 | 547.5 | 352.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-30 | 9.3 | 354.9 | 333.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-31 | 9.3 | 751.8 | 340.3 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-32 | 9.3 | 444.4 | 341.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-33 | 9.3 | 401.4 | 337.2 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-34 | 9.3 | 405.7 | 328.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-35 | 9.3 | 306.8 | 324.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-36 | 9.3 | 293.6 | 323.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-37 | 9.3 | 279.6 | 430.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-38 | 9.3 | 273.0 | 288.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-39 | 9.3 | 321.8 | 287.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-40 | 9.3 | 270.7 | 322.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-05_task-mer_acq-left_run-41 | 9.3 | 266.8 | 330.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-06_task-mer_acq-left_run-01 | 15.4 | 10824.1 | 11102.3 | bad | near flat: std 15.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-02 | 9.4 | 278.2 | 315.0 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-03 | 9.4 | 286.3 | 383.5 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-04 | 9.4 | 832.9 | 426.1 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-05 | 9.4 | 455.4 | 327.9 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-06 | 9.4 | 308.9 | 411.4 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-07 | 9.4 | 299.6 | 434.7 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-08 | 9.4 | 339.5 | 656.5 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-09 | 9.4 | 626.8 | 627.7 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-10 | 9.4 | 350.7 | 587.1 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-11 | 9.4 | 329.9 | 398.4 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-12 | 9.4 | 392.5 | 406.3 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-13 | 9.4 | 1788.1 | 436.4 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-14 | 9.4 | 365.8 | 548.3 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-15 | 9.4 | 341.6 | 488.9 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-16 | 9.4 | 382.0 | 620.0 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-17 | 9.4 | 294.5 | 468.3 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-18 | 9.4 | 311.6 | 611.6 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-19 | 9.4 | 309.8 | 750.5 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-20 | 9.4 | 349.1 | 547.5 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-21 | 9.4 | 424.4 | 506.5 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-22 | 9.4 | 462.2 | 517.5 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-23 | 9.4 | 426.3 | 520.0 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-24 | 9.4 | 394.9 | 572.0 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-25 | 9.4 | 400.1 | 542.7 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-26 | 9.4 | 354.5 | 536.4 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-27 | 9.4 | 397.9 | 1271.1 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-28 | 9.5 | 480.7 | 842.1 | bad | near flat: std 9.5 counts (< 100) |
| sub-06_task-mer_acq-left_run-29 | 9.4 | 433.3 | 1763.7 | bad | near flat: std 9.4 counts (< 100) |
| sub-06_task-mer_acq-left_run-30 | 9.5 | 480.4 | 667.5 | bad | near flat: std 9.5 counts (< 100) |
| sub-06_task-mer_acq-left_run-31 | 9.5 | 460.0 | 818.2 | bad | near flat: std 9.5 counts (< 100) |
| sub-06_task-mer_acq-left_run-32 | 9.5 | 392.4 | 886.4 | bad | near flat: std 9.5 counts (< 100) |
| sub-06_task-mer_acq-left_run-33 | 9.5 | 338.0 | 565.9 | bad | near flat: std 9.5 counts (< 100) |
| sub-06_task-mer_acq-left_run-34 | 9.5 | 351.3 | 437.3 | bad | near flat: std 9.5 counts (< 100) |
| sub-06_task-mer_acq-left_run-35 | 9.5 | 427.7 | 487.4 | bad | near flat: std 9.5 counts (< 100) |
| sub-06_task-mer_acq-left_run-36 | 9.6 | 341.0 | 3002.4 | bad | near flat: std 9.6 counts (< 100) |
| sub-06_task-mer_acq-left_run-37 | 9.6 | 332.4 | 827.5 | bad | near flat: std 9.6 counts (< 100) |
| sub-06_task-mer_acq-left_run-38 | 9.5 | 311.1 | 458.6 | bad | near flat: std 9.5 counts (< 100) |
| sub-06_task-mer_acq-left_run-39 | 9.5 | 326.2 | 541.3 | bad | near flat: std 9.5 counts (< 100) |
| sub-06_task-mer_acq-left_run-40 | 9.6 | 289.8 | 330.2 | bad | near flat: std 9.6 counts (< 100) |
| sub-07_task-mer_acq-left_run-01 | 9.1 | 409.3 | 291.9 | bad | near flat: std 9.1 counts (< 100) |
| sub-07_task-mer_acq-left_run-02 | 9.1 | 398.6 | 296.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-07_task-mer_acq-left_run-03 | 9.1 | 405.5 | 299.3 | bad | near flat: std 9.1 counts (< 100) |
| sub-07_task-mer_acq-left_run-04 | 9.1 | 318.3 | 304.3 | bad | near flat: std 9.1 counts (< 100) |
| sub-07_task-mer_acq-left_run-05 | 9.2 | 326.1 | 302.4 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-06 | 9.2 | 444.1 | 328.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-07 | 9.1 | 283.6 | 322.4 | bad | near flat: std 9.1 counts (< 100) |
| sub-07_task-mer_acq-left_run-08 | 9.2 | 269.5 | 309.4 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-09 | 9.1 | 327.2 | 322.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-07_task-mer_acq-left_run-10 | 9.2 | 363.1 | 325.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-11 | 9.2 | 359.6 | 309.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-12 | 9.2 | 588.7 | 326.7 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-13 | 9.2 | 517.1 | 314.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-14 | 9.2 | 542.6 | 325.1 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-15 | 9.2 | 411.1 | 315.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-16 | 9.2 | 695.5 | 308.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-17 | 9.2 | 544.0 | 285.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-18 | 9.2 | 366.9 | 285.0 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-19 | 9.2 | 1705.2 | 336.7 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-20 | 9.2 | 451.3 | 300.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-21 | 9.2 | 513.3 | 311.4 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-22 | 9.2 | 489.0 | 303.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-23 | 9.2 | 577.2 | 294.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-24 | 9.2 | 527.9 | 321.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-25 | 9.2 | 342.0 | 301.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-26 | 9.2 | 420.6 | 304.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-27 | 9.2 | 419.2 | 306.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-28 | 9.2 | 389.1 | 308.6 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-29 | 9.2 | 355.4 | 298.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-07_task-mer_acq-left_run-30 | 9.2 | 292.0 | 289.3 | bad | near flat: std 9.2 counts (< 100) |
| sub-08_task-mer_acq-left_run-01 | 219.6 | 275.8 | 972.9 | good | n/a |
| sub-08_task-mer_acq-left_run-02 | 7183.8 | 8297.8 | 276.3 | good | n/a |
| sub-08_task-mer_acq-left_run-03 | 232.0 | 5589.1 | 7722.5 | good | n/a |
| sub-08_task-mer_acq-left_run-04 | 219.2 | 288.0 | 596.2 | good | n/a |
| sub-08_task-mer_acq-left_run-05 | 302.3 | 330.2 | 235.6 | good | n/a |
| sub-08_task-mer_acq-left_run-06 | 218.9 | 610.7 | 755.2 | good | n/a |
| sub-08_task-mer_acq-left_run-07 | 656.2 | 355.2 | 234.3 | good | n/a |
| sub-08_task-mer_acq-left_run-08 | 219.1 | 305.2 | 646.6 | good | n/a |
| sub-08_task-mer_acq-left_run-09 | 717.4 | 333.9 | 234.8 | good | n/a |
| sub-08_task-mer_acq-left_run-10 | 219.1 | 297.9 | 535.7 | good | n/a |
| sub-08_task-mer_acq-left_run-11 | 639.3 | 316.2 | 234.7 | good | n/a |
| sub-08_task-mer_acq-left_run-12 | 570.4 | 319.5 | 234.2 | good | n/a |
| sub-08_task-mer_acq-left_run-13 | 438.1 | 396.2 | 234.6 | good | n/a |
| sub-08_task-mer_acq-left_run-14 | 218.8 | 301.9 | 364.0 | good | n/a |
| sub-08_task-mer_acq-left_run-15 | 392.9 | 341.9 | 233.8 | good | n/a |
| sub-08_task-mer_acq-left_run-16 | 219.3 | 345.3 | 349.1 | good | n/a |
| sub-08_task-mer_acq-left_run-17 | 416.0 | 340.0 | 235.3 | good | n/a |
| sub-08_task-mer_acq-left_run-18 | 218.8 | 328.8 | 350.4 | good | n/a |
| sub-08_task-mer_acq-left_run-19 | 219.0 | 310.4 | 338.5 | good | n/a |
| sub-08_task-mer_acq-left_run-20 | 220.4 | 361.0 | 364.4 | good | n/a |
| sub-08_task-mer_acq-left_run-21 | 290.8 | 332.9 | 252.5 | good | n/a |
| sub-08_task-mer_acq-left_run-22 | 219.8 | 316.0 | 322.9 | good | n/a |
| sub-08_task-mer_acq-left_run-23 | 219.5 | 323.2 | 321.7 | good | n/a |
| sub-08_task-mer_acq-left_run-24 | 438.7 | 375.1 | 259.9 | good | n/a |
| sub-08_task-mer_acq-left_run-25 | 219.4 | 320.0 | 308.5 | good | n/a |
| sub-08_task-mer_acq-left_run-26 | 508.4 | 316.1 | 237.4 | good | n/a |
| sub-08_task-mer_acq-left_run-27 | 219.7 | 314.0 | 327.3 | good | n/a |
| sub-08_task-mer_acq-left_run-28 | 660.7 | 337.3 | 240.7 | good | n/a |
| sub-08_task-mer_acq-left_run-29 | 218.8 | 370.1 | 371.6 | good | n/a |
| sub-08_task-mer_acq-left_run-30 | 219.4 | 325.2 | 454.5 | good | n/a |
| sub-08_task-mer_acq-left_run-31 | 219.2 | 344.9 | 441.5 | good | n/a |
| sub-08_task-mer_acq-left_run-32 | 219.0 | 396.1 | 680.3 | good | n/a |
| sub-08_task-mer_acq-left_run-33 | 218.5 | 315.0 | 316.5 | good | n/a |
| sub-08_task-mer_acq-right_run-01 | 226.3 | 2466.0 | 2361.9 | good | n/a |
| sub-08_task-mer_acq-right_run-02 | 219.3 | 329.7 | 311.8 | good | n/a |
| sub-08_task-mer_acq-right_run-03 | 219.8 | 373.7 | 311.4 | good | n/a |
| sub-08_task-mer_acq-right_run-04 | 220.1 | 439.8 | 322.2 | good | n/a |
| sub-08_task-mer_acq-right_run-05 | 239.7 | 595.9 | 565.5 | good | n/a |
| sub-08_task-mer_acq-right_run-06 | 221.0 | 554.3 | 345.3 | good | n/a |
| sub-08_task-mer_acq-right_run-07 | 223.8 | 488.8 | 335.0 | good | n/a |
| sub-08_task-mer_acq-right_run-08 | 226.1 | 679.4 | 389.5 | good | n/a |
| sub-08_task-mer_acq-right_run-09 | 231.9 | 2655.1 | 3074.7 | good | n/a |
| sub-08_task-mer_acq-right_run-10 | 219.9 | 516.7 | 323.8 | good | n/a |
| sub-08_task-mer_acq-right_run-11 | 220.4 | 809.1 | 321.6 | good | n/a |
| sub-08_task-mer_acq-right_run-12 | 222.2 | 681.6 | 365.4 | good | n/a |
| sub-08_task-mer_acq-right_run-13 | 221.6 | 570.0 | 358.8 | good | n/a |
| sub-08_task-mer_acq-right_run-14 | 220.3 | 596.1 | 369.7 | good | n/a |
| sub-08_task-mer_acq-right_run-15 | 220.1 | 471.5 | 325.8 | good | n/a |
| sub-08_task-mer_acq-right_run-16 | 221.2 | 498.4 | 378.0 | good | n/a |
| sub-08_task-mer_acq-right_run-17 | 221.8 | 528.3 | 374.7 | good | n/a |
| sub-08_task-mer_acq-right_run-18 | 230.1 | 816.1 | 437.7 | good | n/a |
| sub-08_task-mer_acq-right_run-19 | 220.6 | 572.4 | 354.4 | good | n/a |
| sub-08_task-mer_acq-right_run-20 | 224.2 | 790.8 | 404.6 | good | n/a |
| sub-08_task-mer_acq-right_run-21 | 220.6 | 474.6 | 368.8 | good | n/a |
| sub-08_task-mer_acq-right_run-22 | 223.6 | 419.9 | 408.5 | good | n/a |
| sub-08_task-mer_acq-right_run-23 | 220.8 | 398.3 | 353.1 | good | n/a |
| sub-08_task-mer_acq-right_run-24 | 220.3 | 407.9 | 347.9 | good | n/a |
| sub-08_task-mer_acq-right_run-25 | 220.3 | 466.7 | 360.4 | good | n/a |
| sub-08_task-mer_acq-right_run-26 | 220.2 | 405.5 | 508.0 | good | n/a |
| sub-08_task-mer_acq-right_run-27 | 220.5 | 555.4 | 340.5 | good | n/a |
| sub-08_task-mer_acq-right_run-28 | 220.4 | 423.1 | 335.1 | good | n/a |
| sub-08_task-mer_acq-right_run-29 | 220.2 | 312.8 | 416.6 | good | n/a |
| sub-08_task-mer_acq-right_run-30 | 220.7 | 402.2 | 336.3 | good | n/a |
| sub-08_task-mer_acq-right_run-31 | 220.1 | 278.1 | 419.1 | good | n/a |
| sub-08_task-mer_acq-right_run-32 | 220.2 | 299.7 | 319.7 | good | n/a |
| sub-08_task-mer_acq-right_run-33 | 220.1 | 280.1 | 418.3 | good | n/a |
| sub-08_task-mer_acq-right_run-34 | 220.2 | 300.4 | 318.6 | good | n/a |
| sub-08_task-mer_acq-right_run-35 | 220.1 | 295.0 | 384.6 | good | n/a |
| sub-08_task-mer_acq-right_run-36 | 220.1 | 278.8 | 422.9 | good | n/a |
| sub-08_task-mer_acq-right_run-37 | 220.0 | 320.8 | 327.7 | good | n/a |
| sub-08_task-mer_acq-right_run-38 | 219.8 | 282.3 | 440.8 | good | n/a |
| sub-08_task-mer_acq-right_run-39 | 219.5 | 297.1 | 350.5 | good | n/a |
| sub-08_task-mer_acq-right_run-40 | 238.7 | 362.9 | 516.7 | good | n/a |
| sub-08_task-mer_acq-right_run-41 | 222.8 | 808.9 | 2347.5 | good | n/a |
| sub-08_task-mer_acq-right_run-42 | 290.4 | 690.9 | 1060.0 | good | n/a |
| sub-08_task-mer_acq-right_run-43 | 219.1 | 272.0 | 384.6 | good | n/a |
| sub-09_task-mer_acq-left_run-01 | 4.8 | 1983.3 | 1835.5 | bad | near flat: std 4.8 counts (< 100) |
| sub-09_task-mer_acq-left_run-02 | 4.7 | 432.9 | 377.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-03 | 4.7 | 645.7 | 429.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-04 | 4.7 | 542.4 | 592.9 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-05 | 4.7 | 468.1 | 371.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-06 | 4.7 | 649.3 | 636.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-07 | 4.7 | 955.1 | 409.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-08 | 4.7 | 1107.2 | 310.7 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-09 | 4.7 | 823.2 | 326.0 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-10 | 4.7 | 443.3 | 501.5 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-11 | 4.7 | 468.8 | 720.8 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-12 | 4.7 | 465.1 | 553.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-13 | 4.7 | 312.6 | 601.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-14 | 4.7 | 286.9 | 490.1 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-15 | 4.7 | 275.3 | 782.7 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-16 | 4.7 | 277.5 | 531.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-17 | 4.7 | 280.2 | 990.5 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-18 | 4.7 | 289.7 | 525.1 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-19 | 4.7 | 295.2 | 895.7 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-20 | 4.7 | 294.2 | 454.7 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-21 | 4.7 | 296.9 | 794.9 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-22 | 4.7 | 302.5 | 533.9 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-23 | 4.7 | 320.2 | 845.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-24 | 4.7 | 321.2 | 1197.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-25 | 4.7 | 346.4 | 1212.7 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-26 | 4.7 | 329.6 | 571.5 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-27 | 4.7 | 312.5 | 875.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-28 | 4.7 | 314.8 | 628.5 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-29 | 4.7 | 307.8 | 636.5 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-30 | 4.7 | 320.8 | 850.5 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-31 | 4.7 | 304.1 | 891.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-32 | 4.7 | 303.0 | 553.8 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-33 | 4.7 | 304.5 | 435.7 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-34 | 4.7 | 295.4 | 380.9 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-35 | 4.7 | 292.0 | 460.0 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-left_run-36 | 4.8 | 286.3 | 424.2 | bad | near flat: std 4.8 counts (< 100) |
| sub-09_task-mer_acq-left_run-37 | 4.8 | 282.7 | 420.3 | bad | near flat: std 4.8 counts (< 100) |
| sub-09_task-mer_acq-left_run-38 | 4.8 | 281.3 | 297.6 | bad | near flat: std 4.8 counts (< 100) |
| sub-09_task-mer_acq-right_run-01 | 5.6 | 4146.5 | 4734.0 | bad | near flat: std 5.6 counts (< 100) |
| sub-09_task-mer_acq-right_run-02 | 4.7 | 506.0 | 354.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-03 | 4.7 | 506.0 | 354.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-04 | 4.7 | 546.2 | 405.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-05 | 4.7 | 607.8 | 390.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-06 | 4.6 | 465.2 | 342.6 | bad | near flat: std 4.6 counts (< 100) |
| sub-09_task-mer_acq-right_run-07 | 4.7 | 409.9 | 329.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-08 | 4.7 | 342.2 | 280.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-09 | 4.7 | 449.5 | 282.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-10 | 4.7 | 793.4 | 338.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-11 | 4.7 | 472.9 | 369.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-12 | 15.9 | 1221.2 | 6956.5 | bad | near flat: std 15.9 counts (< 100) |
| sub-09_task-mer_acq-right_run-13 | 4.7 | 475.7 | 407.9 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-14 | 4.7 | 466.0 | 497.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-15 | 4.7 | 630.7 | 479.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-16 | 4.7 | 485.8 | 654.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-17 | 4.7 | 405.1 | 547.1 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-18 | 4.7 | 413.9 | 679.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-19 | 4.7 | 657.8 | 638.9 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-20 | 4.7 | 454.6 | 1185.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-21 | 4.7 | 478.6 | 916.8 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-22 | 4.6 | 427.6 | 576.0 | bad | near flat: std 4.6 counts (< 100) |
| sub-09_task-mer_acq-right_run-23 | 4.7 | 460.9 | 573.1 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-24 | 4.7 | 347.5 | 681.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-25 | 4.7 | 472.4 | 1044.7 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-26 | 4.7 | 534.9 | 928.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-27 | 4.7 | 490.0 | 585.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-28 | 4.7 | 501.7 | 497.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-29 | 4.7 | 409.7 | 564.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-30 | 4.6 | 438.7 | 452.7 | bad | near flat: std 4.6 counts (< 100) |
| sub-09_task-mer_acq-right_run-31 | 4.7 | 427.9 | 475.0 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-32 | 4.7 | 375.8 | 456.0 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-33 | 4.7 | 359.9 | 398.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-34 | 4.7 | 391.4 | 364.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-35 | 4.7 | 367.9 | 358.5 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-36 | 4.7 | 493.9 | 398.8 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-37 | 4.7 | 486.2 | 416.7 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-38 | 4.7 | 390.5 | 425.8 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-39 | 4.7 | 430.8 | 439.7 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-40 | 4.7 | 476.4 | 679.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-09_task-mer_acq-right_run-41 | 4.7 | 320.7 | 396.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-10_task-mer_acq-left_run-01 | 8.0 | 3587.2 | 2470.0 | bad | near flat: std 8.0 counts (< 100) |
| sub-10_task-mer_acq-left_run-02 | 7.5 | 274.0 | 325.8 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-03 | 7.5 | 294.4 | 305.7 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-04 | 7.5 | 306.9 | 298.8 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-05 | 7.5 | 421.7 | 295.5 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-06 | 7.5 | 337.7 | 304.6 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-07 | 7.5 | 313.0 | 331.9 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-08 | 7.5 | 308.8 | 298.2 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-09 | 7.5 | 338.5 | 302.0 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-10 | 7.5 | 410.0 | 296.8 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-11 | 7.5 | 452.9 | 303.8 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-12 | 7.5 | 294.2 | 296.4 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-13 | 7.5 | 1228.1 | 304.3 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-14 | 7.5 | 341.1 | 269.3 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-15 | 7.5 | 514.4 | 276.9 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-16 | 7.5 | 368.8 | 298.1 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-17 | 7.5 | 353.0 | 441.5 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-18 | 7.5 | 359.3 | 452.3 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-19 | 7.5 | 315.8 | 793.8 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-20 | 7.5 | 372.4 | 488.7 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-21 | 7.5 | 507.9 | 701.8 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-22 | 7.5 | 455.1 | 894.3 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-23 | 7.5 | 358.2 | 856.4 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-24 | 7.5 | 357.6 | 749.3 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-25 | 7.5 | 353.7 | 679.7 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-26 | 7.5 | 355.8 | 1511.4 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-27 | 7.5 | 461.1 | 731.4 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-28 | 7.5 | 497.6 | 989.2 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-29 | 7.5 | 352.0 | 513.6 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-30 | 7.5 | 386.9 | 1152.5 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-31 | 7.5 | 391.4 | 689.9 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-32 | 7.5 | 439.9 | 493.5 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-33 | 7.5 | 629.9 | 660.5 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-34 | 7.5 | 553.5 | 825.8 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-35 | 7.5 | 630.5 | 1347.4 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-36 | 7.5 | 439.4 | 552.6 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-37 | 7.5 | 561.3 | 758.7 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-38 | 7.5 | 441.3 | 475.1 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-39 | 7.5 | 345.4 | 701.9 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-40 | 7.6 | 452.6 | 613.7 | bad | near flat: std 7.6 counts (< 100) |
| sub-10_task-mer_acq-left_run-41 | 7.5 | 437.8 | 949.4 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-42 | 7.5 | 399.3 | 731.8 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-43 | 7.5 | 1314.2 | 858.3 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-44 | 7.5 | 290.0 | 1032.1 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-45 | 7.5 | 291.2 | 656.0 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-46 | 7.5 | 283.5 | 381.7 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-left_run-47 | 7.5 | 287.2 | 350.7 | bad | near flat: std 7.5 counts (< 100) |
| sub-10_task-mer_acq-right_run-01 | 8.4 | 436.5 | 1397.4 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-02 | 8.4 | 297.7 | 933.0 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-03 | 8.4 | 287.0 | 991.7 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-04 | 8.4 | 279.3 | 393.2 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-05 | 8.4 | 287.7 | 495.6 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-06 | 8.4 | 276.9 | 381.1 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-07 | 8.4 | 311.6 | 352.2 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-08 | 8.4 | 300.6 | 350.3 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-09 | 8.4 | 306.9 | 333.2 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-10 | 8.4 | 420.6 | 332.1 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-11 | 8.4 | 449.4 | 328.7 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-12 | 8.4 | 503.5 | 383.6 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-13 | 8.4 | 502.7 | 722.0 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-14 | 8.4 | 808.7 | 341.7 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-15 | 8.4 | 467.9 | 343.9 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-16 | 8.4 | 525.2 | 331.7 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-17 | 8.4 | 494.1 | 350.4 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-18 | 8.4 | 334.1 | 356.1 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-19 | 8.4 | 337.1 | 355.9 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-20 | 8.4 | 322.4 | 349.9 | bad | near flat: std 8.4 counts (< 100) |
| sub-10_task-mer_acq-right_run-21 | 8.3 | 377.1 | 341.4 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-22 | 8.3 | 349.4 | 348.2 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-23 | 8.3 | 346.7 | 343.1 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-24 | 8.3 | 307.2 | 339.6 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-25 | 8.3 | 293.7 | 336.6 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-26 | 8.3 | 743.5 | 430.1 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-27 | 8.3 | 317.6 | 486.0 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-28 | 8.3 | 321.6 | 370.8 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-29 | 8.3 | 383.3 | 401.4 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-30 | 8.3 | 302.0 | 376.3 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-31 | 8.3 | 667.0 | 410.5 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-32 | 8.3 | 360.2 | 402.2 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-33 | 8.3 | 282.8 | 477.7 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-34 | 8.3 | 282.0 | 1251.3 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-35 | 8.3 | 275.8 | 507.3 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-36 | 8.3 | 304.3 | 301.8 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-37 | 8.3 | 277.3 | 665.6 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-38 | 8.3 | 285.0 | 331.9 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-39 | 8.3 | 285.6 | 350.2 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-40 | 8.3 | 283.5 | 345.2 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-41 | 8.3 | 272.4 | 330.6 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-42 | 8.3 | 273.5 | 313.1 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-43 | 8.3 | 273.8 | 305.1 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-44 | 8.3 | 271.7 | 309.2 | bad | near flat: std 8.3 counts (< 100) |
| sub-10_task-mer_acq-right_run-45 | 8.3 | 300.2 | 365.4 | bad | near flat: std 8.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-01 | 9.3 | 365.7 | 408.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-02 | 10.4 | 3981.3 | 4155.9 | bad | near flat: std 10.4 counts (< 100) |
| sub-11_task-mer_acq-left_run-03 | 9.3 | 268.7 | 1714.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-04 | 9.3 | 260.6 | 824.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-05 | 9.3 | 265.9 | 1079.3 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-06 | 9.3 | 259.2 | 1001.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-07 | 9.3 | 255.1 | 720.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-08 | 9.3 | 261.2 | 707.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-09 | 9.3 | 263.0 | 1671.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-10 | 9.3 | 264.0 | 1941.3 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-11 | 9.3 | 274.6 | 1447.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-12 | 9.3 | 275.2 | 974.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-13 | 9.3 | 279.8 | 724.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-14 | 9.3 | 283.4 | 1144.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-15 | 9.3 | 289.1 | 875.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-16 | 9.3 | 300.4 | 917.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-17 | 9.3 | 290.6 | 621.2 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-18 | 9.3 | 293.1 | 694.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-19 | 9.3 | 292.1 | 583.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-20 | 9.3 | 320.7 | 1210.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-21 | 9.3 | 303.8 | 486.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-22 | 9.3 | 314.6 | 381.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-23 | 9.3 | 329.7 | 369.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-24 | 9.3 | 353.5 | 387.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-25 | 9.3 | 549.0 | 422.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-26 | 9.3 | 1285.4 | 428.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-27 | 9.3 | 568.7 | 396.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-28 | 9.3 | 444.1 | 400.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-29 | 9.3 | 405.6 | 389.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-30 | 9.3 | 388.8 | 389.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-31 | 9.3 | 408.0 | 355.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-32 | 9.3 | 358.2 | 345.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-33 | 9.4 | 281.8 | 349.8 | bad | near flat: std 9.4 counts (< 100) |
| sub-11_task-mer_acq-left_run-34 | 9.4 | 278.5 | 338.1 | bad | near flat: std 9.4 counts (< 100) |
| sub-11_task-mer_acq-left_run-35 | 9.3 | 288.6 | 335.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-11_task-mer_acq-left_run-36 | 9.4 | 282.4 | 318.7 | bad | near flat: std 9.4 counts (< 100) |
| sub-11_task-mer_acq-left_run-37 | 9.3 | 285.7 | 317.2 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-01 | 9.5 | 4425.4 | 3207.5 | bad | near flat: std 9.5 counts (< 100) |
| sub-12_task-mer_acq-left_run-02 | 9.2 | 408.9 | 295.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-left_run-03 | 9.3 | 794.9 | 306.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-04 | 9.2 | 1156.5 | 307.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-left_run-05 | 9.3 | 419.4 | 308.3 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-06 | 9.4 | 362.8 | 328.2 | bad | near flat: std 9.4 counts (< 100) |
| sub-12_task-mer_acq-left_run-07 | 9.3 | 319.5 | 338.3 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-08 | 9.3 | 342.8 | 315.3 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-09 | 9.3 | 371.0 | 328.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-10 | 9.3 | 501.4 | 356.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-11 | 9.3 | 407.3 | 560.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-12 | 9.3 | 823.0 | 650.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-13 | 9.3 | 460.3 | 529.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-14 | 9.3 | 505.6 | 737.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-15 | 9.3 | 384.9 | 493.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-16 | 9.3 | 496.1 | 542.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-17 | 9.3 | 329.6 | 589.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-18 | 9.3 | 783.4 | 486.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-19 | 9.3 | 322.8 | 403.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-20 | 9.3 | 339.7 | 397.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-21 | 9.3 | 361.3 | 507.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-22 | 9.3 | 427.4 | 405.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-23 | 9.3 | 375.9 | 414.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-24 | 9.3 | 400.3 | 394.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-25 | 9.3 | 328.7 | 369.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-26 | 9.7 | 368.1 | 404.9 | bad | near flat: std 9.7 counts (< 100) |
| sub-12_task-mer_acq-left_run-27 | 9.3 | 336.8 | 367.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-28 | 9.3 | 362.9 | 439.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-29 | 9.3 | 363.4 | 468.2 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-30 | 9.3 | 351.4 | 332.3 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-31 | 10.5 | 328.2 | 337.4 | bad | near flat: std 10.5 counts (< 100) |
| sub-12_task-mer_acq-left_run-32 | 9.3 | 393.4 | 339.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-33 | 9.3 | 443.8 | 352.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-34 | 9.3 | 311.1 | 351.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-35 | 9.3 | 320.6 | 348.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-36 | 9.3 | 641.8 | 366.2 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-37 | 9.3 | 456.8 | 343.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-38 | 9.3 | 305.6 | 365.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-39 | 9.3 | 291.1 | 353.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-left_run-40 | 9.5 | 253.2 | 303.8 | bad | near flat: std 9.5 counts (< 100) |
| sub-12_task-mer_acq-left_run-41 | 9.4 | 254.0 | 305.0 | bad | near flat: std 9.4 counts (< 100) |
| sub-12_task-mer_acq-right_run-01 | 9.9 | 3693.7 | 4929.0 | bad | near flat: std 9.9 counts (< 100) |
| sub-12_task-mer_acq-right_run-02 | 9.3 | 330.3 | 308.3 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-03 | 9.2 | 326.6 | 334.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-04 | 9.3 | 549.1 | 313.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-05 | 9.3 | 328.3 | 343.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-06 | 9.3 | 1441.2 | 338.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-07 | 9.3 | 418.9 | 401.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-08 | 9.2 | 382.4 | 715.3 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-09 | 9.2 | 363.0 | 481.9 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-10 | 9.3 | 524.2 | 459.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-11 | 9.2 | 401.5 | 578.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-12 | 9.3 | 470.3 | 547.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-13 | 9.3 | 373.1 | 931.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-14 | 9.3 | 376.6 | 742.2 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-15 | 9.2 | 432.2 | 426.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-16 | 9.3 | 722.5 | 1075.9 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-17 | 9.2 | 391.6 | 397.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-18 | 9.3 | 559.7 | 907.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-19 | 9.3 | 357.1 | 388.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-20 | 9.3 | 864.6 | 415.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-21 | 9.3 | 419.3 | 586.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-22 | 9.3 | 395.1 | 432.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-23 | 9.2 | 370.1 | 594.1 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-24 | 9.2 | 439.4 | 323.3 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-25 | 9.2 | 365.3 | 338.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-26 | 9.3 | 390.0 | 330.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-27 | 9.2 | 418.3 | 357.5 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-28 | 9.3 | 413.7 | 331.1 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-29 | 9.3 | 374.6 | 300.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-30 | 9.2 | 340.7 | 315.2 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-31 | 9.6 | 442.4 | 319.2 | bad | near flat: std 9.6 counts (< 100) |
| sub-12_task-mer_acq-right_run-32 | 9.3 | 344.1 | 338.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-33 | 9.3 | 311.5 | 345.0 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-34 | 9.3 | 372.3 | 361.6 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-35 | 9.3 | 307.4 | 341.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-36 | 9.6 | 283.6 | 373.9 | bad | near flat: std 9.6 counts (< 100) |
| sub-12_task-mer_acq-right_run-37 | 9.3 | 299.0 | 344.3 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-38 | 9.3 | 279.5 | 333.8 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-39 | 9.3 | 266.7 | 342.7 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-40 | 9.2 | 263.1 | 307.1 | bad | near flat: std 9.2 counts (< 100) |
| sub-12_task-mer_acq-right_run-41 | 9.3 | 263.0 | 291.5 | bad | near flat: std 9.3 counts (< 100) |
| sub-12_task-mer_acq-right_run-42 | 9.3 | 266.1 | 307.4 | bad | near flat: std 9.3 counts (< 100) |
| sub-13_task-mer_acq-left_run-01 | 4.7 | 322.3 | 400.0 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-left_run-02 | 4.8 | 343.8 | 316.1 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-03 | 5.7 | 5908.0 | 4869.9 | bad | near flat: std 5.7 counts (< 100) |
| sub-13_task-mer_acq-left_run-04 | 4.8 | 382.1 | 303.9 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-05 | 4.8 | 335.8 | 316.5 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-06 | 4.8 | 304.7 | 317.6 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-07 | 4.8 | 313.4 | 299.3 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-08 | 4.8 | 304.8 | 296.1 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-09 | 4.8 | 315.8 | 295.4 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-10 | 4.8 | 474.7 | 298.5 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-11 | 4.8 | 853.1 | 301.7 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-12 | 4.8 | 637.2 | 305.1 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-13 | 4.8 | 529.0 | 322.0 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-14 | 4.8 | 515.7 | 315.9 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-15 | 4.8 | 472.7 | 307.9 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-16 | 4.8 | 703.8 | 306.8 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-17 | 4.8 | 705.0 | 309.5 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-18 | 4.8 | 520.8 | 296.4 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-19 | 4.8 | 391.7 | 304.4 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-20 | 4.8 | 351.3 | 323.8 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-21 | 4.8 | 358.5 | 316.4 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-22 | 4.8 | 445.2 | 327.7 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-23 | 4.8 | 400.1 | 364.8 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-24 | 4.8 | 381.5 | 335.7 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-25 | 4.8 | 411.8 | 344.2 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-26 | 4.8 | 616.2 | 322.8 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-27 | 4.8 | 484.6 | 327.0 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-28 | 4.8 | 476.8 | 268.1 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-29 | 4.8 | 549.2 | 291.5 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-30 | 4.8 | 1694.9 | 316.5 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-31 | 4.8 | 408.1 | 376.1 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-32 | 4.8 | 383.3 | 386.6 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-33 | 4.8 | 367.2 | 300.3 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-34 | 4.8 | 353.9 | 353.1 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-35 | 4.8 | 503.7 | 381.0 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-36 | 4.8 | 466.7 | 298.0 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-37 | 4.8 | 442.2 | 308.9 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-38 | 4.8 | 318.8 | 306.1 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-39 | 4.8 | 296.4 | 311.8 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-40 | 4.8 | 288.3 | 306.6 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-41 | 4.8 | 290.6 | 294.2 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-42 | 4.8 | 279.7 | 325.0 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-43 | 4.8 | 275.7 | 295.0 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-44 | 4.8 | 272.6 | 293.1 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-45 | 4.8 | 268.3 | 301.1 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-46 | 4.8 | 265.0 | 291.3 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-left_run-47 | 4.8 | 265.5 | 286.2 | bad | near flat: std 4.8 counts (< 100) |
| sub-13_task-mer_acq-right_run-01 | 9.2 | 9462.4 | 10127.8 | bad | near flat: std 9.2 counts (< 100) |
| sub-13_task-mer_acq-right_run-02 | 4.7 | 1404.7 | 298.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-03 | 4.6 | 473.3 | 299.0 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-04 | 4.6 | 513.5 | 318.0 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-05 | 4.6 | 782.6 | 323.5 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-06 | 4.6 | 624.9 | 334.9 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-07 | 4.6 | 475.2 | 362.5 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-08 | 4.6 | 693.7 | 318.2 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-09 | 4.6 | 940.2 | 342.8 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-10 | 4.6 | 417.4 | 314.0 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-11 | 4.6 | 395.9 | 310.9 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-12 | 4.6 | 423.8 | 302.1 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-13 | 4.6 | 357.7 | 281.2 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-14 | 4.6 | 397.4 | 304.7 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-15 | 4.6 | 465.1 | 374.3 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-16 | 4.7 | 623.6 | 368.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-17 | 4.7 | 589.0 | 318.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-18 | 4.6 | 495.3 | 325.2 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-19 | 4.7 | 454.8 | 316.0 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-20 | 4.6 | 521.6 | 324.3 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-21 | 4.7 | 688.1 | 334.8 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-22 | 4.7 | 641.2 | 322.9 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-23 | 4.6 | 564.5 | 311.2 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-24 | 4.7 | 407.2 | 301.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-25 | 4.7 | 518.6 | 329.6 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-26 | 4.7 | 489.3 | 324.0 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-27 | 4.7 | 413.6 | 345.9 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-28 | 4.6 | 376.8 | 349.0 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-29 | 4.7 | 375.4 | 331.0 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-30 | 4.6 | 320.8 | 328.0 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-31 | 4.6 | 307.3 | 317.2 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-32 | 4.7 | 356.5 | 354.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-33 | 4.7 | 316.9 | 338.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-34 | 4.7 | 298.4 | 324.3 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-35 | 4.7 | 297.2 | 338.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-36 | 4.7 | 540.4 | 508.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-37 | 4.7 | 287.1 | 337.2 | bad | near flat: std 4.7 counts (< 100) |
| sub-13_task-mer_acq-right_run-38 | 4.6 | 333.6 | 328.9 | bad | near flat: std 4.6 counts (< 100) |
| sub-13_task-mer_acq-right_run-39 | 4.7 | 288.2 | 339.4 | bad | near flat: std 4.7 counts (< 100) |
| sub-14_task-mer_acq-right_run-01 | 9.1 | 268.7 | 655.9 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-02 | 9.0 | 272.4 | 544.5 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-03 | 9.0 | 276.5 | 606.1 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-04 | 9.0 | 299.2 | 358.2 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-05 | 9.0 | 270.3 | 401.6 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-06 | 9.0 | 274.7 | 479.0 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-07 | 9.0 | 270.9 | 581.7 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-08 | 9.0 | 273.9 | 458.1 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-09 | 9.0 | 292.1 | 543.0 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-10 | 9.1 | 283.6 | 357.2 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-11 | 9.0 | 308.5 | 327.3 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-12 | 9.1 | 552.4 | 316.8 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-13 | 9.0 | 621.1 | 311.1 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-14 | 9.0 | 399.4 | 294.4 | bad | near flat: std 9.0 counts (< 100) |
| sub-14_task-mer_acq-right_run-15 | 9.1 | 383.9 | 301.3 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-16 | 9.1 | 542.5 | 330.2 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-17 | 9.1 | 405.4 | 351.1 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-18 | 9.1 | 496.9 | 346.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-19 | 9.1 | 373.8 | 347.6 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-20 | 9.1 | 634.7 | 335.1 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-21 | 9.1 | 623.8 | 328.0 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-22 | 9.1 | 384.6 | 320.9 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-23 | 9.1 | 278.8 | 311.2 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-24 | 9.1 | 277.5 | 314.2 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-25 | 10.3 | 1963.7 | 2404.3 | bad | near flat: std 10.3 counts (< 100) |
| sub-14_task-mer_acq-right_run-26 | 9.1 | 280.1 | 295.6 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-27 | 9.1 | 289.4 | 289.7 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-28 | 9.1 | 303.4 | 302.1 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-29 | 9.1 | 364.4 | 362.3 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-30 | 9.1 | 344.9 | 344.1 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-31 | 9.1 | 318.2 | 333.9 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-32 | 9.1 | 311.5 | 322.2 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-33 | 9.1 | 296.1 | 311.2 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-34 | 9.1 | 349.5 | 321.7 | bad | near flat: std 9.1 counts (< 100) |
| sub-14_task-mer_acq-right_run-35 | 9.1 | 295.2 | 317.4 | bad | near flat: std 9.1 counts (< 100) |

</details>

The per-run table gives `status` and `status_description` of Electrode1 exactly as in the PR's `channels.tsv` (692 `bad`
rows; Electrode2/3 stay `good`). The summary gives the README and CHANGES figures and the PR description's "the Zenodo .mat
files have the same values".

**Coverage**: 830 of 830 files (2490 of 2490 channels), including the Zenodo comparison.

Reproduce: `python code/receipts/2026-10-22_flat-electrode1.py <nm000406 root> --zenodo-zip <data.zip>` (Python 3.15.0,
numpy 2.5.4, pandas 3.1.0, scipy 1.18.1; MNE not used).
