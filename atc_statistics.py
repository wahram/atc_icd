# calculate how often a specific drug has been prescribed
import csv

file = open('atc_icd_excluded.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader, None)

interesting_codes = ['C02AC05', 'C02LC05']
info = {}

for code in interesting_codes:
    info[code] = 0

data = []
for row in reader:
    data.append(dict(zip(headers, row)))

for row in data:
    score = 0
# Wie würde man die Reihe 01 02 03 04 05 06 07 08 09 10 11 12 .... schlau darstellen? https://stackoverflow.com/questions/134934/display-number-with-leading-zeros If i < 10: s = "0" + int(i) oder mit .format
    atc_codes = []
    for pos in range(1, 9 + 1):
        row_name = 'atc_0' + str(pos)
        if row[row_name] in interesting_codes:
            info[row[row_name]] += 1
    for pos in range(10, 25 + 1):
        row_name = 'atc_' + str(pos)
        if row[row_name] in interesting_codes:
            info[row[row_name]] += 1
print(info)
