import os
import csv

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_text(text, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

def save_csv(data, output_file):
    lines = data.splitlines()
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        for line in lines:
            # Split each line by commas and write to the CSV
            print(line)
            writer.writerow(line.split(","))
