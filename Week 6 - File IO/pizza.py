import sys
import csv
from tabulate import tabulate
import os

def read_pinocchio_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            table = list(csvreader)
    except FileNotFoundError:
        sys.exit(f"File does not exist")
    except Exception as e:
        sys.exit(f"Error reading CSV file: {e}")

    return table

def main():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith('.csv'):
        sys.exit("Not a CSV file")

    if not os.path.isfile(file_path):
        sys.exit("File does not exist")

    table = read_pinocchio_csv(file_path)

    if table:
        print(tabulate(table, headers='firstrow', tablefmt='grid'))

if __name__ == "__main__":
    main()
