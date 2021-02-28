# calculates probability for having coronary artery disease
import csv
from atcs import *
from icd import is_cad

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

nitrat = ranolazin | organic_nitrates
# trapidil
# platelet_aggregation_inhibitor
# selective_betablocker
# statin, ezetimib
# ace_inhibitor
# at1_antagonist

cad_contraindicated = celecoxib | etoricoxib | parecoxib | diclofenac | triptan

file = open('validation.csv')
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

    if platelet_aggregation_inhibitor & atc_codes and (statin & atc_codes or ezetimib & atc_codes) \
            and (at1_antagonist & atc_codes or ace_inhibitor & atc_codes or selective_betablocker & atc_codes):
        score += 100

    if score == 0:
        cad_unlikely += 1
    elif score <= 50:
        cad_possible += 1
    elif score < 100:
        cad_probable += 1
    else:
        cad_positive += 1

    if score >= threshold and any([is_cad(icd) for icd in icd_codes]):
        true_positive += 1
        if cad_contraindicated & atc_codes:
            highrisk_prescription_identified +=1
            print(row)
    if score >= threshold and not any([is_cad(icd) for icd in icd_codes]):
        false_positive += 1
        if cad_contraindicated & atc_codes:
            highrisk_prescription_identified +=1
            print('False Positive', row)
    if score < threshold and not any([is_cad(icd) for icd in icd_codes]):
        true_negative += 1
    if score < threshold and any([is_cad(icd) for icd in icd_codes]):
        false_negative += 1

try:
    specificity = true_negative / (true_negative + false_positive)
except:
    specificity = 1

try:
    sensitivity = true_positive / (true_positive + false_negative)
except:
    sensitivity = 1
print('CAD unlikely:', cad_unlikely, 'CAD possible:', cad_possible, 'CAD probable:', cad_probable, 'CAD positive:',
      cad_positive)
print('True Positives:', true_positive, 'True Negatives:', true_negative, 'False Positives:', false_positive,
      'False Negatives:', false_negative)  # validation: CAD(true) - true_positive = false_negative
print('alpha-error:', false_positive / (false_positive + true_negative), 'beta-error:',
      false_negative / (false_negative + true_positive))
print('Specificity:', specificity)
print('Sensitivity:', sensitivity)
print('PPV:', true_positive / (true_positive + false_positive))
print('NPV:', true_negative / (true_negative + false_negative))
print('FDR:', false_positive / (true_positive + false_positive))
print('Precision:', true_positive / (true_positive + false_positive))
print('Recall:', true_positive / (true_positive + false_negative))
print('Positive:', true_positive + false_negative)
print('Negative:', true_negative + false_positive)

print('High risk Prescriptions:', highrisk_prescription_identified)