# calculates probability for having coronary artery disease
from atc_codes import load_codes
import csv
from atcs import *
from icd import is_cad

threshold = 10

highrisk_prescription_identified = 0
cad_unlikely = 0
cad_possible = 0
cad_probable = 0
cad_positive = 0

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

nitrat = ranolazin | ismn | isdn | molsidomin | pentaerythrityltetranitrat
p2y12_inhibitor = clopidogrel | prasugrel | ticagrelor
betablocker = metoprolol | bisoprolol | carvedilol | atenolol | nebivolol
statin = lovastatin | pravastatin | simvastatin | atorvastatin | rosuvastatin
ace_hemmer = captopril | enalapril | lisinopril | ramipril
at1_antagonist =

cad_contraindicated = celecoxib | etoricoxib | parecoxib | diclofenac_systemic | almotriptan | eletriptan | frovatriptan | naratriptan | \
                      rizatriptan | sumatriptan | zolmitriptan

file = open('atc_icd_inplausible_excluded.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader)

codes = load_codes('ATC_Codes.csv')
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

    if score >= threshold and any([is_cad(icd) for icd in icd_codes]):
        true_positive += 1
        if cad_contraindicated & atc_codes:
            highrisk_prescription_identified +=1
            print(row)
    if score >= threshold and not any([is_cad(icd) for icd in icd_codes]):
        false_positive += 1
        if cad_contraindicated & atc_codes:
            highrisk_prescription_identified +=1
    if score < threshold and not any([is_cad(icd) for icd in icd_codes]):
        true_negative += 1
    if score < threshold and any([is_cad(icd) for icd in icd_codes]):
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

print('High risk Prescriptions:', highrisk_prescription_identified)
