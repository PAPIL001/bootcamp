
import csv

def filter_csv(file_name, condition):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if condition(row):
                yield row

# Example usage: Filter rows where the first column is greater than 50
for row in filter_csv('data.csv', lambda r: int(r[0]) > 50):
    print(row)
