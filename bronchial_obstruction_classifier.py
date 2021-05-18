# identifies patients with bronchial obstruction and contraindications
import csv
from atcs import *
from math import sqrt
from icd import is_bronchial_obstruction

highrisk_prescription_identified = 0

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

bronchial_obstruction_treatment = aclidinium | aminophylline | benralizumab | ciclesonide | fenoterol | formoterol |\
                                  indacaterol | ipratropium | mepolizumab | montelukast | olodaterol | omalizumab |\
                                  reproterol | reslizumab | roflumilast | salbutamol | salmeterol | terbutaline |\
                                  theophylline | tiotropium | umeclidinium
bronchial_obstruction_contraindicated = sotalol | dextrometorphan | carvedilol | metoprolol | propranolol | atenolol

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

    if bronchial_obstruction_treatment & atc_codes and any([is_bronchial_obstruction(icd) for icd in icd_codes]):
        true_positive += 1

    if bronchial_obstruction_treatment & atc_codes and not any([is_bronchial_obstruction(icd) for icd in icd_codes]):
        false_positive += 1

    if not bronchial_obstruction_treatment & atc_codes and any([is_bronchial_obstruction(icd) for icd in icd_codes]):
        false_negative += 1

    if not bronchial_obstruction_treatment & atc_codes and not any([is_bronchial_obstruction(icd) for icd in icd_codes]):
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
      specificity - 1.959964 * sqrt(specificity * (1 - specificity) / (true_negative + false_positive)),
      specificity + 1.959964 * sqrt(specificity * (1 - specificity) / (true_negative + false_positive)))  # 95% confidence interval
print('Sensitivity:', sensitivity,
      sensitivity - 1.959964 * sqrt(sensitivity * (1 - sensitivity) / (true_positive + false_negative)),
      sensitivity + 1.959964 * sqrt(sensitivity * (1 - sensitivity) / (true_positive + false_negative)))
print('PPV:', ppv, ppv - 1.959964 * sqrt(ppv * (1 - ppv) / (true_positive + false_positive)),
      ppv + 1.959964 * sqrt(ppv * (1 - ppv) / (true_positive + false_positive)))
print('NPV:', npv, npv - 1.959964 * sqrt(npv * (1 - npv) / (true_negative + false_negative)),
      npv + 1.959964 * sqrt(npv * (1 - npv) / (true_negative + false_negative)))
print('High risk Prescriptions:', highrisk_prescription_identified)

print('True Positives:', true_positive, 'True Negatives:', true_negative, 'False Positives:', false_positive,
      'False Negatives:', false_negative)  # validation: bronchial_obstruction(true) - true_positive = false_negative

precision = ppv
recall = sensitivity
print('Precision:', precision, 'Recall:', recall, 'F1', 2 * precision * recall / (precision + recall))
