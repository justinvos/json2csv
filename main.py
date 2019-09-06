import csv
import json
import sys

def convert (json_file_path, csv_file_path):
  items = []
  with open(json_file_path) as json_file:
    items = json.load(json_file)

  headers = list(items[0].keys())
  rows = make_rows(headers, items)

  with open(csv_file_path, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)

def make_rows (headers, items):
  rows = [headers]
  for item in items:
    row = []
    for header in headers:
      row += [item[header]]
    rows += [row]
  return rows

convert(sys.argv[1], sys.argv[2])
