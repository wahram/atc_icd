# calculate how often a specific drug has been prescribed
import csv

file = open('atc_icd_inplausible_excluded.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader, None)

interesting_codes = ['C09AA01', 'C09AA02', 'C09AA03', 'C09AA04', 'C09AA05', 'C09AA06', 'C09AA07', 'C09AA08', 'C09AA09',
                     'C09AA10', 'C09AA11', 'C09AA12', 'C09AA13', 'C09AA14', 'C09AA15', 'C09AA16']
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
print(info)
