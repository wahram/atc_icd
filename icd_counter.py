# calculate how often a specific ICD-Code occurs. Note: I20.0 != I20.00
import csv

file = open('test_2338.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader, None)

interesting_codes = ['I10.0']

info = {}

for code in interesting_codes:
    info[code] = 0

data = []
for row in reader:
    data.append(dict(zip(headers, row)))

for row in data:
    icd_codes = set()
    for pos in range(1, 20 + 1):
        row_name = 'icd10_%02d' % pos
        if row[row_name] in interesting_codes:
            info[row[row_name]] += 1
print(info)
