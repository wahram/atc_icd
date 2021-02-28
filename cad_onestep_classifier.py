# identifies patients with cad and contraindications by one-step approach
import csv
from atcs import *

highrisk_prescription_identified = 0

cad_treatment = ranolazin | organic_nitrates
cad_contraindicated = celecoxib | etoricoxib | parecoxib | diclofenac | triptan

file = open('test.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader, None)

data = []
for row in reader:
    data.append(dict(zip(headers, row)))

for row in data:

    atc_codes = set()
    for pos in range(1, 25 + 1):
        row_name = 'atc_%02d' % pos
        if row[row_name]:
            atc_codes.add(row[row_name])

    icd_codes = set()
    for pos in range(1, 20 + 1):
        row_name = 'icd10_%02d' % pos
        if row[row_name]:
            icd_codes.add(row[row_name])

    if cad_treatment & atc_codes and cad_contraindicated & atc_codes:
        highrisk_prescription_identified += 1
        print(row)

print('High risk Prescriptions:', highrisk_prescription_identified)