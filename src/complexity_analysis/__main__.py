from pathlib import Path

from src.complexity_analysis.commits_per_file_analyzer import count_commits_in_repo
from src.complexity_analysis.lines_of_code_analyzer import count_lines_of_python_files

if __name__ == "__main__":
    top_n = 10

    commit_counts = count_commits_in_repo(Path("../../transformers"), "2023-01-01")
    sorted_commit_counts = sorted(commit_counts.items(), key=lambda item: item[1], reverse=True)[:top_n]

    line_counts = count_lines_of_python_files(Path("../transformers"))
    sorted_line_counts = sorted(line_counts.items(), key=lambda item: item[1], reverse=True)[:top_n]

    header = "| Top n | File Name | Commits / Lines of Code (LoC) | Bar |\n"
    separator = "|-----------|-----------|-----------|------------|\n"
    rows = header + separator
    for i in range(top_n):
        commit_count_file_name = sorted_commit_counts[i][0]
        commit_count = sorted_line_counts[i][1]

        lines_count_file_name = sorted_line_counts[i][0]
        lines_count = sorted_commit_counts[i][1]

        bar = f"*" * (commit_count // 70)
        rows += f"| {i + 1} | {commit_count_file_name} | Commits: {commit_count:,} | {bar} |\n"

        bar = f"*" * (lines_count // 70)
        rows += f"| {i + 1} | {lines_count_file_name} | LoC: {lines_count:,} | {bar} |\n"

    Path("../docs/LoC_and_NCC.md").open("w", encoding="utf-8").write(rows)