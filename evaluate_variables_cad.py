# establish different specifity and sensitivity pairs with their variables for CAD algorithm
from atc_codes import load_codes
import csv
from atcs import *
import sys
from itertools import product

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

CAD = ['I20.0', 'I20.00', 'I20.8', 'I20.9',
       'I21.0', 'I21.1', 'I21.3', 'I21.4', 'I21.9',
       'I23.6',
       'I24.8', 'I24.9',
       'I25.0', 'I25.11', 'I25.12', 'I25.13', 'I25.19', 'I25.29', 'I25.5', 'I25.9']

print([n for n in CAD if 19 < int(n.split('.')[0][1:]) < 26])
exit()


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



for ranolazin_score in range(0, 101, 50):
    for nitrat_score in range(0, 101, 50):
        for trapidil_score in range(0, 101, 50):
            for ass_score in range(0, 101, 50):
                for p2y12_inhibitor_score in range(0, 101, 50):
                    for betablocker_score in range(0, 101, 50):
                        for calciumkanalblocker_score in range(0, 101, 50):
                            for statin_score in range(0, 101, 50):
                                for ezetimib_score in range(0, 101, 50):
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

                                        if score >= 100 and any(item in CAD for item in row.values()):
                                            true_positive += 1
                                        if score >= 100 and not any(item in CAD for item in row.values()):
                                            false_positive += 1
                                        if score < 100 and not any(item in CAD for item in row.values()):
                                            true_negative += 1
                                        if score < 100 and any(item in CAD for item in row.values()):
                                            false_negative += 1

                                    original_stdout = sys.stdout  # Save a reference to the original standard output
                                    with open('CAD_result.txt', 'a') as f:
                                        print('Specificity:', true_negative / (true_negative + false_positive),
                                            'Sensitivity:', true_positive / (true_positive + false_negative+0.00001),
                                            ranolazin_score, nitrat_score, trapidil_score, ass_score,
                                            p2y12_inhibitor_score, betablocker_score, calciumkanalblocker_score,
                                            statin_score, ezetimib_score, file=f) # avoid division by zero

                                        print('True Positives:', true_positive, 'True Negatives:', true_negative,
                                              'False Positives:', false_positive,
                                              'False Negatives:',
                                              false_negative)  # validation: CAD(true) - true_positive = false_negative
                                        true_positive = 0
                                        true_negative = 0
                                        false_positive = 0
                                        false_negative = 0