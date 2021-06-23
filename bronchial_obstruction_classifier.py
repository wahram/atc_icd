# identifies patients with bronchial obstruction and contraindications
import csv

import statsmodels.api as statsmodels

from atcs import *
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

file = open('atc_icd_implausible_excluded_validated.csv')
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
    for pos in range(1, 25 + 1):
        row_name = 'icd10_%02d' % pos
        if row[row_name]:
            icd_codes.add(row[row_name])

    if bronchial_obstruction_treatment & atc_codes and bronchial_obstruction_contraindicated & atc_codes\
            and any([is_bronchial_obstruction(icd) for icd in icd_codes]):
        highrisk_prescription_identified += 1

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

