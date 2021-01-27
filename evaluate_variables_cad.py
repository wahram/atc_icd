# establish different specifity and sensitivity pairs with their variables for CAD algorithm
from atc_codes import load_codes
import csv
from atcs import *
import sys
from itertools import product
from cli import progress
from icd import is_cad

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

nitrat = ranolazin | ismn | isdn | molsidomin | pentaerythrityltetranitrat
p2y12_inhibitor = clopidogrel | prasugrel | ticagrelor
betablocker = metoprolol | bisoprolol | carvedilol | atenolol | nebivolol
calciumkanalblocker = verapamil | diltiazem | nifedipin | amlodipin | lercanidipin | felodipin
statin = lovastatin | pravastatin | simvastatin | atorvastatin | rosuvastatin

file = open('atc_icd_excluded.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader)

codes = load_codes('ATC_Codes.csv')
data = []
for row in reader:
    data.append(dict(zip(headers, row)))



params = list(product(
    [i for i in range(0, 101, 50)], # ranolazin
    [i for i in range(0, 101, 50)], # nitrat
    [i for i in range(0, 101, 50)], # trapidil
    [i for i in range(0, 101, 50)], # ass
    [i for i in range(0, 101, 50)], # p2y12_inhibitor
    [i for i in range(0, 101, 50)], # betablocker
    [i for i in range(0, 101, 50)], # calciumkanalblocker
    [i for i in range(0, 101, 50)], # statin
    [i for i in range(0, 101, 50)]  # ezetimib
))

params_max = len(params)
cycle_counter = 0
for param in params:
    ranolazin_score, nitrat_score, trapidil_score, ass_score, p2y12_inhibitor_score, betablocker_score, \
    calciumkanalblocker_score, statin_score, ezetimib_score = param

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

        if ranolazin & atc_codes:
            score += ranolazin_score

        if nitrat & atc_codes:
            score += nitrat_score

        if trapidil & atc_codes:
            score += trapidil_score

        if ass & atc_codes:
            score += ass_score

        if p2y12_inhibitor & atc_codes:
            score += p2y12_inhibitor_score

        if betablocker & atc_codes:
            score += betablocker_score

        if calciumkanalblocker & atc_codes:
            score += calciumkanalblocker_score

        if statin & atc_codes:
            score += statin_score

        if ezetimib & atc_codes:
            score += ezetimib_score

        if score >= 100 and any([is_cad(icd) for icd in icd_codes]):
            true_positive += 1
        if score >= 100 and not any([is_cad(icd) for icd in icd_codes]):
            false_positive += 1
        if score < 100 and not any([is_cad(icd) for icd in icd_codes]):
            true_negative += 1
        if score < 100 and any([is_cad(icd) for icd in icd_codes]):
            false_negative += 1

    original_stdout = sys.stdout  # Save a reference to the original standard output
    with open('CAD_result3.txt', 'a') as f:
        try:
            specificity = true_negative / (true_negative + false_positive)
        except:
            specificity = 1

        try:
            sensitivity = true_positive / (true_positive + false_negative)
        except:
            sensitivity = 1

        print('Specificity:', specificity,
              'Sensitivity:', sensitivity,
              ranolazin_score, nitrat_score, trapidil_score, ass_score,
              p2y12_inhibitor_score, betablocker_score, calciumkanalblocker_score,
              statin_score, ezetimib_score, file=f)
        print('True Positives:', true_positive, 'True Negatives:', true_negative,
              'False Positives:', false_positive,
              'False Negatives:',
              false_negative)  # validation: CAD(true) - true_positive = false_negative
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
        cycle_counter += 1
        progress(params_max, cycle_counter)