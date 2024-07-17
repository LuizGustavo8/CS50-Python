import csv
import sys
import os

def scourgify(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as infile:
            reader = csv.DictReader(infile)
            data = []
            for row in reader:
                try:
                    last_name, first_name = row['name'].split(', ')
                    house = row['house']
                    data.append({'first': first_name, 'last': last_name, 'house': house})
                except ValueError:
                    sys.exit("Error: Invalid format in input file")

        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
        sys.exit(f"Error: The file '{input_file}' does not exist")
    except Exception as e:
        sys.exit(f"Error processing files: {e}")

def main():

    # Validate command-line arguments
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Validate file extension
    if not input_file.endswith('.csv') or not output_file.endswith('.csv'):
        sys.exit("Error: Both input and output files must have a .csv extension")

    # Process the CSV files
    scourgify(input_file, output_file)

if __name__ == "__main__":
    main()
