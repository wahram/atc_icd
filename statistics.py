# print values of interesting diagnoses.
import csv

file = open('atc_icd_excluded.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader, None)

interesting_columns = ['icd10_01']
info = {}

for col in interesting_columns:
    info[col] = {}

data = []
for row in reader:
    data.append(dict(zip(headers, row)))

for row in data:
    for col in interesting_columns:

        if not row[col] in info[col]:
            info[col][row[col]] = 0

        info[col][row[col]] += 1

for name, data in info.items():
    print(name, data)