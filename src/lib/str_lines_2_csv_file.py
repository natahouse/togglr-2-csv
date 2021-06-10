# from os import getcwd
from typing import List


def str_lines_2_csv_file(file_path: str, str_lines: List[str]):
    file = open(file_path, "w")

    new_line = "\n"
    full_csv = new_line.join(str_lines)

    file.write(full_csv)
    file.close()
