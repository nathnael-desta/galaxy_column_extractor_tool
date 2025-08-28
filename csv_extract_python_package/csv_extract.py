import csv
import sys
import argparse

def main():
    # Use argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description="Extract specific columns from a CSV file.")
    parser.add_argument('--input', required=True, help='Input CSV file path.')
    parser.add_argument('--columns', required=True, help='Comma-separated column numbers (1-based).')
    parser.add_argument('--output', required=True, help='Output CSV file path.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()

    try:
        # Convert column numbers to 0-based indices
        column_indices = [int(col.strip()) - 1 for col in args.columns.split(',')]

        with open(args.input, 'r', newline='') as infile, \
                open(args.output, 'w', newline='') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                # Handle rows that might be shorter than an expected index
                new_row = [row[i] for i in column_indices if i < len(row)]
                writer.writerow(new_row)
        
        print("Successfully extracted columns.")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
