

import sys
import os

def count_lines_of_code(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    code_lines = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#'):
            code_lines += 1

    return code_lines

def main():


    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    lines_of_code = count_lines_of_code(filename)
    print(f"{lines_of_code}")

if __name__ == "__main__":
    main()
