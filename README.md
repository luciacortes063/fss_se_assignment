## Task 1: Defect Analysis

### Extracting Commit Data
We collected all commits after **2023-01-01** and identified defect-related commits using the keywords:
- fix
- bug
- error
- issue
- hotfix
- resolve
- repair

Each commit was parsed to extract its date, message, and modified files.  
We also built a complete month timeline from the entire commit history, so months with zero defects (like October 2025) would still appear in the plots.

### Total Number of Defects per Month
The plot shows a more or less stable activity in 2023 and 2024, followed by a clear increase in early and mid-2025. However in October 2025, the number of defect-related commits drops sharply to 0.

**Why does the number of defects drop sharply in October 2025?**  
When we inspected the commits for October 2025, we found that only two commits were made in that month, and both were strictly release-related:
- 8ac2b916b0 | 2025-10-03 | Release: v4.57.0
- 2ccc6cae21 | 2025-10-03 | v4.57.0 Branch (#41310)
So no regular development or bug-fixing work happened during this period.
This suggests that early October 2025 corresponds to the release freeze and publication of v4.57.0, a phase where teams typically avoid functional changes.
As a result, almost no defect-related commits were recorded, which explains the sharp drop in the plot.


### Most Defective Files
The two files with the highest number of defect-related commits are:

1. `src/transformers/modeling_utils.py`  
2. `src/transformers/trainer.py`

We plotted the monthly defect counts for both files (the plot can be found in `fss_se_assignment.ipynb`).

**In which month were the most defects introduced for each file?**

- **modeling_utils.py:** The highest peak appears in February-March 2025, where the file receives a large cluster of defect-fix commits.  
- **trainer.py:** The highest peak occurs in June 2023, with a clear spike compared to surrounding months.

### Why these peaks?

For `src/transformers/modeling_utils.py` in March 2025, the commit history shows a combination of new features, refactors, and several bug fixes touching core modeling and attention components. For instance:

- `"[Feature] Support using FlashAttention2 on Ascend NPU (#36696)"`  
- `"Refactor Attention implementation for ViT-based models (#36545)"`  
- `"fix torch_dtype, contiguous, and load_state_dict regression (#36512)"`  

This mix of heavy feature work and regression fixes indicates a period of intense development, which explains the spike in defect-related commits for that file.

For `src/transformers/trainer.py` in June 2023, almost every commit relates to training stability, checkpoint handling, distributed training, or scheduler behavior. Some examples are:

- `"fix peft ckpts not being pushed to hub (#24578)"`  
- `"Fix LR scheduler based on bs from auto bs finder (#24521)"`  
- `"Replace DataLoader logic for Accelerate in Trainer (#24028)"`  

These commits modify fundamental parts of the training workflow, so it makes sense that this month shows the highest concentration of fixes for `trainer.py`.


### Limitations of This Method
This approach based on keywords has several limitations:

- Bug fixes that don’t mention our keywords are not detected, and the method also misses variations such as plurals (“bugs”, “issues”) or different verb forms (“fixed”, “fixing”). As a result, several legitimate defect-related commits may not be captured.

- Commits that say “fix typo” or “improve error message” get counted as defects even if they are not real bug fixes, which can lead to false positives. 

- All defects count the same, because small fixes and major bugs contribute equally.

- There is a weak connection between defects and files, because if a commit touches several files, all of them get counted even if the fix concerns only one. 

- This approach depends on commit message quality. It relies entirely on how consistently developers write their messages.

For these reasons, the method is useful for spotting general trends but cannot precisely identify all defective hotspots.

