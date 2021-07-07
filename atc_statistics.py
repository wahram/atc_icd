# calculate how often a specific drug has been prescribed
import csv

file = open('atc_icd_implausible_excluded_validated_deleted.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader, None)

interesting_codes = ['C09DX04']
info = {}

for code in interesting_codes:
    info[code] = 0

data = []
for row in reader:
    data.append(dict(zip(headers, row)))

for row in data:
    atc_codes = set()
    for pos in range(1, 25 + 1):
        row_name = 'atc_%02d' % pos
        if row[row_name] in interesting_codes:
            info[row[row_name]] += 1
            print(row)
print(info)
