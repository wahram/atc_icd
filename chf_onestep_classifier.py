# identifies patients with chf and contraindications by one-step approach
import csv

import statsmodels.api as statsmodels

from atcs import *
from icd import is_chf

highrisk_prescription_identified = 0

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

chf_treatment = sacubitril_valsartan | eplerenon
chf_contraindicated = celecoxib | diclofenac | domperidon | dronedaron | eletriptan | etoricoxib \
                             | flecainid | methylphenidat | moxonidin | parecoxib | pioglitazon | tadalafil \
                             | cilostazol | desmopressin | fludrocortison

file = open('atc_icd_implausible_excluded_validated_deleted.csv')
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

    if chf_treatment & atc_codes and any([is_chf(icd) for icd in icd_codes]) and chf_contraindicated & atc_codes:
        highrisk_prescription_identified += 1

    if chf_treatment & atc_codes and any([is_chf(icd) for icd in icd_codes]):
        true_positive += 1

    if chf_treatment & atc_codes and not any([is_chf(icd) for icd in icd_codes]):
        false_positive += 1

    if not chf_treatment & atc_codes and any([is_chf(icd) for icd in icd_codes]):
        false_negative += 1

    if not chf_treatment & atc_codes and not any([is_chf(icd) for icd in icd_codes]):
        true_negative += 1

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
      'False Negatives:', false_negative)  # validation: CHF(true) - true_positive = false_negative

precision = ppv
recall = sensitivity
print('Precision:', precision, 'Recall:', recall, 'F1', 2 * precision * recall / (precision + recall))