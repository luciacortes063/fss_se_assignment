# Task 2: Complexity Analysis
Measuring complexity is useful in many cases, like pinpointing refactoring opportunities, 
and a number of different metrics exist for this task, which are shown in Table 1.
A complexity hotspot is a file that might be problematic due to its high complexity.
With that in mind, complete the following analysis:

## Select two complexity metrics of your choice
Selected metrics are:
- Lines of code (LoC)
- Number of code changes (NCC)

## Calculate the complexity of all .py files in the repository using the selected metrics

### Line count - top 10 files:

| Count | File Name |
|-----------|------------|
| 6172 | tests/trainer/test_trainer.py |
| 5333 | src/transformers/trainer.py |
| 4978 | tests/generation/test_utils.py |
| 4683 | src/transformers/modeling_utils.py |
| 4672 | tests/test_tokenization_common.py |
| 4342 | src/transformers/models/seamless_m4t_v2/modeling_seamless_m4t_v2.py |
| 4331 | src/transformers/tokenization_utils_base.py |
| 4265 | src/transformers/models/qwen2_5_omni/modular_qwen2_5_omni.py |
| 4096 | tests/test_modeling_common.py |
| 4090 | src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py |

For complete results see: [Lines count table](line_count_table.md)

### Code changes (commits) - top 10 files:

| Count | File Name |
|-----------|------------|
| 595 | src/transformers/modeling_utils.py |
| 497 | src/transformers/trainer.py |
| 424 | src/transformers/__init__.py |
| 380 | src/transformers/generation/utils.py |
| 360 | tests/test_modeling_common.py |
| 305 | src/transformers/models/auto/modeling_auto.py |
| 296 | src/transformers/models/auto/configuration_auto.py |
| 278 | tests/generation/test_utils.py |
| 260 | src/transformers/training_args.py |
| 247 | src/transformers/utils/dummy_pt_objects.py |

For complete results see: [Commits count table](commits_count_table.md)

## Visualize the complexity hotspots. 
The visualization should effectively convey which parts of the code are more complex or change more frequently. 
Feel free to use any visualization of your choice.

Explain the rationale behind your decision:  
- Why words clouds?: Because the bigger words means more occurrences, this is helpful to highlight hot-spots.
- Why bar charts?: In order to compare and quantize results

### Combined results
| Top n | File Name | Commits / Lines of Code (LoC) | Bar |
|-----------|-----------|-----------|------------|
| 1 | src/transformers/modeling_utils.py | Commits: 6,172 | **************************************************************************************** |
| 1 | tests/trainer/test_trainer.py | LoC: 595 | ******** |
| 2 | src/transformers/trainer.py | Commits: 5,333 | **************************************************************************** |
| 2 | src/transformers/trainer.py | LoC: 497 | ******* |
| 3 | src/transformers/__init__.py | Commits: 4,978 | *********************************************************************** |
| 3 | tests/generation/test_utils.py | LoC: 424 | ****** |
| 4 | src/transformers/generation/utils.py | Commits: 4,683 | ****************************************************************** |
| 4 | src/transformers/modeling_utils.py | LoC: 380 | ***** |
| 5 | tests/test_modeling_common.py | Commits: 4,672 | ****************************************************************** |
| 5 | tests/test_tokenization_common.py | LoC: 360 | ***** |
| 6 | src/transformers/models/auto/modeling_auto.py | Commits: 4,342 | ************************************************************** |
| 6 | src/transformers/models/seamless_m4t_v2/modeling_seamless_m4t_v2.py | LoC: 305 | **** |
| 7 | src/transformers/models/auto/configuration_auto.py | Commits: 4,331 | ************************************************************* |
| 7 | src/transformers/tokenization_utils_base.py | LoC: 296 | **** |
| 8 | tests/generation/test_utils.py | Commits: 4,265 | ************************************************************ |
| 8 | src/transformers/models/qwen2_5_omni/modular_qwen2_5_omni.py | LoC: 278 | *** |
| 9 | src/transformers/training_args.py | Commits: 4,096 | ********************************************************** |
| 9 | tests/test_modeling_common.py | LoC: 260 | *** |
| 10 | src/transformers/utils/dummy_pt_objects.py | Commits: 4,090 | ********************************************************** |
| 10 | src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py | LoC: 247 | *** |


### Lines of Code
For the 'src' module:
![Visualization 1](../images/line_counts-src_module.png)
![Visualization 1](../images/line_counts-word_cloud-src_module.png)

For the 'tests' module:
![Visualization 1](../images/line_counts-tests_module.png)
![Visualization 1](../images/line_counts-word_cloud-tests_module.png)


## What can you say about the correlation between the two complexity measures in this repository? 
For the transformers repository there doesn't seem to be a strong correlation between the number of lines of code and commit numbers.
So more lines of code does not imply more commits in this case.

## A colleague of yours claims that “Files with higher complexity tend to be more defective”. What evidence can you present to support or reject this claim for the selected complexity measures in this repository?
Given the metrics we chose there wouldn't be enough evidence in this repo to support this claim.
Higher count of lines could mean a higher code complexity, more defects could mean there are more commits for a concrete file. Since we didn't find
a correlation between these measures, this would be an argument against said friends claim, at least in regard to these two metrics.