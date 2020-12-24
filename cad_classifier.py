# calculates probability for having coronary artery disease
from atc_codes import load_codes
import csv
from atcs import *

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

CAD = ['I20.0', 'I20.00', 'I20.8', 'I20.9',
       'I21.0', 'I21.1', 'I21.3', 'I21.4', 'I21.9',
       'I23.6',
       'I24.8', 'I24.9',
       'I25.0', 'I25.11', 'I25.12', 'I25.13', 'I25.19', 'I25.29', 'I25.5', 'I25.9']

nitrat = ranolazin | ismn | isdn | molsidomin | pentaerythrityltetranitrat
p2y12_inhibitor = clopidogrel | prasugrel | ticagrelor
betablocker = metoprolol | bisoprolol | carvedilol | atenolol | nebivolol
calciumkanalblocker = verapamil | diltiazem | nifedipin | amlodipin | lercanidipin | felodipin
statin = lovastatin | pravastatin | simvastatin | atorvastatin | rosuvastatin
cad_contraindicated = celecoxib | etoricoxib | parecoxib | diclofenac_systemic | almotriptan | eletriptan | frovatriptan | naratriptan | \
                      rizatriptan | sumatriptan | zolmitriptan

file = open('atc_icd_excluded.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader)

codes = load_codes('ATC_Codes.csv')
data = []
for row in reader:
    data.append(dict(zip(headers, row)))

for row in data:
    score = 0

    atc_codes = set()
    for pos in range(1, 9 + 1):
        row_name = 'atc_0' + str(pos)
        if row[row_name]:
            atc_codes.add(row[row_name])
    for pos in range(10, 20 + 1):
        row_name = 'atc_' + str(pos)
        if row[row_name]:
            atc_codes.add(row[row_name])
    if ranolazin & atc_codes or nitrat & atc_codes or trapidil & atc_codes:
        score += 100

    if ass & atc_codes:
        score += 80

    if p2y12_inhibitor & atc_codes:
        score += 15

    if betablocker & atc_codes and calciumkanalblocker & atc_codes:
        score += 5

    if statin & atc_codes or ezetimib & atc_codes:
        score += 5

    if score == 0:
        cad_unlikely += 1
    elif score <= 50:
        cad_possible += 1
    elif score < 100:
        cad_probable += 1
    else:
        cad_positive += 1

    if score >= threshold and any(item in CAD for item in row.values()):
        true_positive += 1
        if cad_contraindicated & atc_codes:
            highrisk_prescription_identified += 1
    if score >= threshold and not any(item in CAD for item in row.values()):
        false_positive += 1
        print(row)
    if score < threshold and not any(item in CAD for item in row.values()):
        true_negative += 1
    if score < threshold and any(item in CAD for item in row.values()):
        false_negative += 1

print('CAD unlikely:', cad_unlikely, 'CAD possible:', cad_possible, 'CAD probable:', cad_probable, 'CAD positive:',
      cad_positive)
print('True Positives:', true_positive, 'True Negatives:', true_negative, 'False Positives:', false_positive,
      'False Negatives:', false_negative)  # validation: CAD(true) - true_positive = false_negative
print('alpha-error:', false_positive / (false_positive + true_negative), 'beta-error:',
      false_negative / (false_negative + true_positive))  # alpha and beta error
print('Specificity:', true_negative / (true_negative + false_positive))  # identify healthy person
print('Sensitivity:', true_positive / (true_positive + false_negative))  # identify ill person
print('PPV:', true_positive / (true_positive + false_positive))
print('NPV:', true_negative / (true_negative + false_negative))
print('FDR:', false_positive / (true_positive + false_positive))
print('Precision:', true_positive / (true_positive + false_positive))
print('Recall:', true_positive / (true_positive + false_negative))
print('Positive:', true_positive + false_negative)
print('Negative:', true_negative + false_positive)

print(highrisk_prescription_identified)
