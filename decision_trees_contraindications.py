# identifies contraindications with decision tree classifier

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

file = open('atc_icd_implausible_excluded_validated.csv')
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
    for pos in range(1, 25 + 1):
        row_name = 'icd10_%02d' % pos
        if row[row_name]:
            icd_codes.add(row[row_name])

    if bronchial_obstruction_contraindicated & atc_codes:
        highrisk_prescription_identified += 1
        print(row)

"""    if any([is_c10aa(atc) for atc in atc_codes]) and any([is_n02ba(atc) for atc in atc_codes]):
        score += 100
    if any([is_c10aa(atc) for atc in atc_codes]) and not any([is_n02ba(atc) for atc in atc_codes]) \
            and any([is_b01ac(atc) for atc in atc_codes]):
        score += 100
    if not any([is_c10aa(atc) for atc in atc_codes]) and any([is_c01da(atc) for atc in atc_codes]):
        score += 100


    if score >= threshold and cad_contraindicated & atc_codes:
        print(row)

    if any([is_cad(icd) for icd in icd_codes]) and cad_contraindicated & atc_codes:
        highrisk_prescription_identified += 1
        print(row)"""



try:
    specificity = true_negative / (true_negative + false_positive)
except:
    specificity = 1

try:
    sensitivity = true_positive / (true_positive + false_negative)
except:
    sensitivity = 1

ppv = true_positive / (true_positive + false_positive)
npv = true_negative / (true_negative + false_negative)
print('Specificity:', specificity,
      statsmodels.stats.proportion_confint(true_negative, true_negative + false_positive, alpha=0.05, method='wilson'))
print('Sensitivity:', sensitivity,
      statsmodels.stats.proportion_confint(true_positive, true_positive + false_negative, alpha=0.05, method='wilson'))
print('PPV:', ppv,
      statsmodels.stats.proportion_confint(true_positive, true_positive + false_positive, alpha=0.05, method='wilson'))
print('NPV:', npv,
      statsmodels.stats.proportion_confint(true_negative, true_negative + false_negative, alpha=0.05, method='wilson'))
print('High risk Prescriptions:', highrisk_prescription_identified)

print('True Positives:', true_positive, 'True Negatives:', true_negative, 'False Positives:', false_positive,
      'False Negatives:', false_negative)  # validation: bronchial_obstruction(true) - true_positive = false_negative

precision = ppv
recall = sensitivity
print('Precision:', precision, 'Recall:', recall, 'F1', 2 * precision * recall / (precision + recall))

