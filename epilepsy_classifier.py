# identifies patients with epilepsy and contraindicated medication
from atc_codes import load_codes
import csv
from atcs import *

highrisk_prescription_identified = 0

epilepsy_treatment = lamotrigin | levetiracetam | valproat
epilepsy_contraindicated = baclofen | dimenhydrinat | levofloxacin | metoclopramid | sulpirid

file = open('atc_icd_inplausible_excluded.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader, None)

codes = load_codes('ATC_Codes.csv')
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

    if epilepsy_treatment & atc_codes and epilepsy_contraindicated & atc_codes:
        highrisk_prescription_identified += 1
        print(row)

print('High risk Prescriptions:', highrisk_prescription_identified)