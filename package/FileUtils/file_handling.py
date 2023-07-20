import csv
import json

def read_file(file_path):
    """
    Read and return the content of a text file.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_to_file(file_path, content):
    """
    Write the given content to a text file.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def append_to_file(file_path, content):
    """
    Append the given content to a text file.
    """
    with open(file_path, 'a') as file:
        file.write(content)

def read_csv(file_path):
    """
    Read and parse a CSV file, returning a list of dictionaries representing the rows.
    """
    rows = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            rows.append(row)
    return rows

def write_csv(file_path, data, fieldnames):
    """
    Write data to a CSV file using the provided fieldnames.
    """
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def read_json(file_path):
    """
    Read and parse a JSON file, returning the parsed data.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    """
    Write data to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def compare_files(file_path1, file_path2):
    """
    Compare the content of two files and return whether they are identical or not.
    """
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        content1 = file1.read()
        content2 = file2.read()
    
    return content1 == content2
