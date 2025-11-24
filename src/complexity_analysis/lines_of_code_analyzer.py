from pathlib import Path

from matplotlib import pyplot as plt
from wordcloud import WordCloud


def _dict_to_markdown_table(input_data: dict[str, int]) -> str:
    header = "| Line Count | File Name |\n"
    separator = "|-----------|------------|\n"
    rows = ""

    for key, value in input_data.items():
        rows += f"| {value} | {key} |\n"

    return header + separator + rows


def count_lines_of_python_files(directory: Path, exclude_venv: bool = True, exclude_empty_init: bool = True) -> dict[str, int]:
    result = {}

    if not directory.exists():
        print(f"ERROR: Directory {directory} does not exist")
        return result

    for file in directory.glob("**/*.py"):
        lines_count = len(file.open("r", encoding='utf-8').readlines())
        relative_file_path = file.relative_to(directory).__str__()

        if exclude_venv and relative_file_path.startswith(".venv"):
            continue
        elif exclude_empty_init and file.name == "__init__.py" and lines_count == 0:
            continue

        result[relative_file_path] = lines_count

    return result


def create_bar_chart(input_data: dict[str, int], output_path: Path, file_name: str, show_top_n_entries: int = 30) -> None:
    output_file = output_path / f"{file_name}.png"
    top_files = sorted(input_data.items(), key=lambda item: item[1], reverse=True)[:show_top_n_entries]
    file_names, line_counts = zip(*top_files)

    plt.figure(figsize=(40, 20))
    plt.barh(file_names, line_counts, color='skyblue')
    plt.title(f"Top {show_top_n_entries} Files by Line Count")
    plt.xlabel("Line Count")
    plt.ylabel("File Name")
    plt.gca().invert_yaxis()
    plt.grid(axis="x")
    plt.savefig(output_file)
    plt.clf()

    print(f"Successfully saved plot under {output_file}")


def create_word_cloud(input_data: dict[str, int], output_path: Path, file_name: str, width: int = 1080, height: int = 720) -> None:
    output_file = output_path / f"{file_name}.png"
    wordcloud = WordCloud(width=width, height=height, background_color="white")
    wordcloud.generate_from_frequencies(input_data)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(output_file)
    plt.clf()

    print(f"Successfully saved plot under {output_file}")


if __name__ == '__main__':
    path_to_repo = Path("../../transformers")
    figures_output_path = Path("../../images")
    md_output_path = Path("../../docs")

    line_counts_total = count_lines_of_python_files(path_to_repo, exclude_venv=False, exclude_empty_init=False)
    line_counts_without_venv_and_empty_init_files = count_lines_of_python_files(path_to_repo)
    line_counts_test_module = {}
    line_counts_src_module = {}

    for key, value in line_counts_without_venv_and_empty_init_files.items():
        if key.startswith("tests"):
            line_counts_test_module[key.replace("tests/", "")] = value
        elif key.startswith("src/transformers"):
            line_counts_src_module[key.replace("src/transformers/", "")] = value

    sorted_line_counts_total = dict(sorted(line_counts_total.items(), key=lambda item: item[1], reverse=True))
    markdown_table = _dict_to_markdown_table(sorted_line_counts_total)
    (md_output_path / "line_count_table.md").open("w", encoding="utf-8").write(markdown_table)

    create_bar_chart(line_counts_src_module, figures_output_path, "line_counts-src_module")
    create_bar_chart(line_counts_test_module, figures_output_path, "line_counts-tests_module")
    create_word_cloud(line_counts_src_module, figures_output_path, "line_counts-word_cloud-src_module")
    create_word_cloud(line_counts_test_module, figures_output_path,"line_counts-word_cloud-tests_module")
