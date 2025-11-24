import subprocess
import os
from pathlib import Path

from src.paths import TRANSFORMERS_REPO_PATH, DOCS_PATH
from src.utility.dict_to_markdown_table import dict_to_markdown_table


def count_commits_in_repo(repo_path: Path, since_date: str) -> dict[str, int]:
    result = {}
    command = f"git log --since='{since_date}' --pretty=format: --name-only"

    os.chdir(repo_path)
    output = subprocess.check_output(command, shell=True, text=True)
    files = output.strip().splitlines()

    for file in files:
        if file and file.endswith('.py'):
            result[file] = result.get(file, 0) + 1

    return result


if __name__ == "__main__":
    commit_counts = count_commits_in_repo(TRANSFORMERS_REPO_PATH, "2023-01-01")
    sorted_commit_counts = dict(sorted(commit_counts.items(), key=lambda item: item[1], reverse=True))

    markdown_table = dict_to_markdown_table(sorted_commit_counts)
    (DOCS_PATH / "commits_count_table.md").open("w", encoding="utf-8").write(markdown_table)
