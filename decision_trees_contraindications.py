# identifies contraindications with decision tree classifier.

import csv

import statsmodels.api as statsmodels

from atcs import *
from icd import *

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

gout_contraindications = 0
epilepsy_contraindications = 0
cad_contraindications = 0
chf_contraindications = 0
bronchial_obstruction_contraindications = 0

threshold = 100

highrisk_prescription_identified = 0

cad_contraindicated = celecoxib | etoricoxib | parecoxib | diclofenac | triptan | fludrocortison
bronchial_obstruction_contraindicated = sotalol | dextrometorphan | carvedilol | metoprolol | propranolol | atenolol
gout_contraindicated = xipamid | hydrochlorothiazid | torasemid
chf_contraindicated = celecoxib | diclofenac | domperidon | dronedaron | eletriptan | etoricoxib \
                             | flecainid | methylphenidat | moxonidin | parecoxib | pioglitazon | tadalafil \
                             | cilostazol | desmopressin | fludrocortison
epilepsy_contraindicated = baclofen | bethanechol | buspiron | dimenhydrinat | diphenhydramin | doxylamin | \
                           levofloxacin | methocarbamol | metoclopramid | ofloxacin_oral | sulpirid | terizidon

file = open('atc_icd_implausible_excluded_validated_deleted.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader)

data = []
for row in reader:
    data.append(dict(zip(headers, row)))

for row in data:
    score = 0

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

    if any([is_r03bb(atc) for atc in atc_codes]) and any([is_c03ba(atc) for atc in atc_codes]) and any([is_b05ba(atc) for atc in atc_codes]):
        if bronchial_obstruction_contraindicated & atc_codes and any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bronchial_obstruction_contraindications += 1

    if not any([is_r03bb(atc) for atc in atc_codes]) and any([is_r03al(atc) for atc in atc_codes]) and any([is_m05bb(atc) for atc in atc_codes]):
        if bronchial_obstruction_contraindicated & atc_codes and any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bronchial_obstruction_contraindications += 1

    if not any([is_r03bb(atc) for atc in atc_codes]) and not any([is_r03al(atc) for atc in atc_codes]) and any([is_r03ak(atc) for atc in atc_codes]):
        if bronchial_obstruction_contraindicated & atc_codes and any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bronchial_obstruction_contraindications += 1


    if not any([is_c03ca(atc) for atc in atc_codes]) and any([is_c01dx(atc) for atc in atc_codes]):
        if chf_contraindicated & atc_codes and any([is_chf(icd) for icd in icd_codes]):
            chf_contraindications += 1

    if not any([is_c03ca(atc) for atc in atc_codes]) and not any([is_c01dx(atc) for atc in atc_codes]) and any([is_s01ed(atc) for atc in atc_codes]):
        if chf_contraindicated & atc_codes and any([is_chf(icd) for icd in icd_codes]):
            chf_contraindications += 1

    if not any([is_c03ca(atc) for atc in atc_codes]) and not any([is_n03ax(atc) for atc in atc_codes]) and any([is_c03da(atc) for atc in atc_codes]):
        if chf_contraindicated & atc_codes and any([is_chf(icd) for icd in icd_codes]):
            chf_contraindications += 1


    if not any([is_c10aa(atc) for atc in atc_codes]) and any([is_c07ab(atc) for atc in atc_codes]):
        if cad_contraindicated & atc_codes and any([is_cad(icd) for icd in icd_codes]):
            cad_contraindications += 1

    if not any([is_c10aa(atc) for atc in atc_codes]) and not any([is_c07ab(atc) for atc in atc_codes]) and any([is_a10ae(atc) for atc in atc_codes]):
        if cad_contraindicated & atc_codes and any([is_cad(icd) for icd in icd_codes]):
            cad_contraindications += 1

    if not any([is_c10aa(atc) for atc in atc_codes]) and not any([is_c07ab(atc) for atc in atc_codes]) and (any([is_c01da(atc) for atc in atc_codes]) or any([is_m01ah(atc) for atc in atc_codes])):
        if cad_contraindicated & atc_codes and any([is_cad(icd) for icd in icd_codes]):
            cad_contraindications += 1


    if not any([is_n03ax(atc) for atc in atc_codes]) and any([is_b03ba(atc) for atc in atc_codes]) and any([is_g04ca(atc) for atc in atc_codes]):
        if epilepsy_contraindicated and any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_contraindications += 1

    if not any([is_n03ax(atc) for atc in atc_codes]) and not any([is_b03ba(atc) for atc in atc_codes]) and any([is_n03af(atc) for atc in atc_codes]):
        if epilepsy_contraindicated and any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_contraindications += 1

    if not any([is_n03ax(atc) for atc in atc_codes]) and any([is_n03ag(atc) for atc in atc_codes]):
        if epilepsy_contraindicated and any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_contraindications += 1


    if any([is_m04aa(atc) for atc in atc_codes]) and gout_contraindicated & atc_codes and any([is_gout(icd) for icd in icd_codes]):
        gout_contraindications += 1

    if not any([is_m04aa(atc) for atc in atc_codes]) and not any([is_n02ab(atc) for atc in atc_codes]) and any([is_a10ac(atc) for atc in atc_codes]) \
            and gout_contraindicated & atc_codes and any([is_gout(icd) for icd in icd_codes]):
        gout_contraindications += 1

print('High risk Prescriptions:', highrisk_prescription_identified)
print('gout contraindications:', gout_contraindications)
print('epilepsy contraindications:', epilepsy_contraindications)
print('CAD contraindications:', cad_contraindications)
print('CHF contraindications:', chf_contraindications)
print('BO contraindications', bronchial_obstruction_contraindications)
