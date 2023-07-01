import json
import csv

def convert_json_to_csv(json_data, csv_file):
    # Load JSON data
    with open(json_data, 'r') as file:
        data = json.load(file)

    # Extract field names from the first JSON object
    fieldnames = list(data[0].keys())

    # Write data to CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header row
        writer.writeheader()

        # Write each JSON object as a row
        writer.writerows(data)

# Example usage:
json_data_file = 'data.json'
csv_file = 'data.csv'
convert_json_to_csv(json_data_file, csv_file)
