import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def convert_csv_to_json():
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    convert_csv_to_json()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

