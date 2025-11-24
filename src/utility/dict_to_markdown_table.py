def dict_to_markdown_table(input_data: dict[str, int]) -> str:
    header = "| Count | File Name |\n"
    separator = "|-----------|------------|\n"
    rows = ""

    for key, value in input_data.items():
        rows += f"| {value} | {key} |\n"

    return header + separator + rows
