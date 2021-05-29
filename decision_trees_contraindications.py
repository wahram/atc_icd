# identifies contraindications with decision tree classifier

import csv
from math import sqrt
from atcs import *

# C07AB is Beta blocking agents, selective
def is_c10aa(atc):
    if not atc:
        return False
    return atc.startswith('C10AA')  # HMG CoA reductase inhibitors


def is_n02ba(atc):
    if not atc:
        return False
    return atc.startswith('N02BA')  # Salicylic acid and derivatives


def is_b01ac(atc):
    if not atc:
        return False
    return atc.startswith('B01AC')  # Platelet aggregation inhibitors excl. heparin


def is_c01da(atc):
    if not atc:
        return False
    return atc.startswith('C01DA')  # Organic nitrates


threshold = 100

highrisk_prescription_identified = 0
cad_unlikely = 0
cad_possible = 0
cad_probable = 0
cad_positive = 0

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

cad_contraindicated = celecoxib | etoricoxib | parecoxib | diclofenac | triptan | fludrocortison

file = open('atc_icd_implausible_excluded_cad_validated.csv')
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
    for pos in range(1, 21 + 1):
        row_name = 'icd10_%02d' % pos
        if row[row_name]:
            icd_codes.add(row[row_name])

    if any([is_c10aa(atc) for atc in atc_codes]) and any([is_n02ba(atc) for atc in atc_codes]):
        score += 100
    if any([is_c10aa(atc) for atc in atc_codes]) and not any([is_n02ba(atc) for atc in atc_codes]) \
            and any([is_b01ac(atc) for atc in atc_codes]):
        score += 100
    if not any([is_c10aa(atc) for atc in atc_codes]) and any([is_c01da(atc) for atc in atc_codes]):
        score += 100




    if score >= threshold and cad_contraindicated & atc_codes:
        highrisk_prescription_identified += 1
        print(row)

    """if score >= threshold and any([is_cad(icd) for icd in icd_codes]):
        true_positive += 1

    if score >= threshold and not any([is_cad(icd) for icd in icd_codes]):
        false_positive += 1

    if not score >= threshold and any([is_cad(icd) for icd in icd_codes]):
        false_negative += 1

    if not score >= threshold and not any([is_cad(icd) for icd in icd_codes]):
        true_negative += 1"""


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

print('CAD unlikely:', cad_unlikely, 'CAD possible:', cad_possible, 'CAD probable:', cad_probable, 'CAD positive:',
      cad_positive)
print('True Positives:', true_positive, 'True Negatives:', true_negative, 'False Positives:', false_positive,
      'False Negatives:', false_negative)  # validation: CAD(true) - true_positive = false_negative
print('alpha-error:', false_positive / (false_positive + true_negative), 'beta-error:',
      false_negative / (false_negative + true_positive))
print('Specificity:', specificity,
      specificity - 1.959964 * sqrt(specificity * (1 - specificity) / (true_negative + false_positive)),
      specificity + 1.959964 * sqrt(specificity * (1 - specificity) / (true_negative + false_positive)))  # 95% confidence interval
print('Sensitivity:', sensitivity,
      sensitivity - 1.959964 * sqrt(sensitivity * (1 - sensitivity) / (true_positive + false_negative)),
      sensitivity + 1.959964 * sqrt(sensitivity * (1 - sensitivity) / (true_positive + false_negative)))
print('PPV:', ppv, ppv - 1.959964 * sqrt(ppv * (1 - ppv) / (true_positive + false_positive)),
      ppv + 1.959964 * sqrt(ppv * (1 - ppv) / (true_positive + false_positive)))
print('NPV:', npv, npv - 1.959964 * sqrt(npv * (1 - npv) / (true_negative + false_negative)),
      npv + 1.959964 * sqrt(npv * (1 - npv) / (true_negative + false_negative)))
print('FDR:', false_positive / (true_positive + false_positive))
print('Precision:', true_positive / (true_positive + false_positive))
print('Recall:', true_positive / (true_positive + false_negative))
print('Positive:', true_positive + false_negative)
print('Negative:', true_negative + false_positive)

print('High risk Prescriptions:', highrisk_prescription_identified)

precision = ppv
recall = sensitivity
print('Precision:', precision, 'Recall:', recall, 'F1', 2 * precision * recall / (precision + recall))
