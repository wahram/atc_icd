# identifies patients with peripheral artery disease and betablocker
import csv
from atcs import *

highrisk_prescription_identified = 0

pavk_treatment = cilostazol | naftidrofuryl
pavk_contraindicated = selective_betablocker | propranolol

file = open('atc_icd_implausible_excluded.csv')
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

    if pavk_treatment & atc_codes and pavk_contraindicated & atc_codes:
        highrisk_prescription_identified += 1
        print(row)

print('High risk Prescriptions:', highrisk_prescription_identified)
