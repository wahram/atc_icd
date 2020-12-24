# establish different specifity and sensitivity pairs with their variables for CHF algorithm

from atc_codes import load_codes
import csv
from atcs import *
import sys

from icd import is_chf

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

sacubitril_valsartan_score = 0
aldosteronantagonist_score = 0
betablocker_score = 0
ivabradin_score = 0
dihydropyridin_score = 0
herzglykosid_score = 0
ace_hemmer_score = 0
ass_score = 0
p2y12_inhibitor_score = 0
schleifendiuretikum_score = 0


aldosteronantagonist = eplerenon | spironolacton
betablocker = metoprolol | bisoprolol | carvedilol | atenolol | nebivolol
dihydropyridin = amlodipin | nifedipin | felodipin | lercanidipin
herzglykosid = digoxin | digitoxin
ace_hemmer = captopril | enalapril | lisinopril | ramipril
hf_drug_without_herzglykosid = sacubitril_valsartan | eplerenon | betablocker | spironolacton | ivabradin | dihydropyridin | ace_hemmer
schleifendiuretikum = furosemid | torasemid
p2y12_inhibitor = clopidogrel | prasugrel | ticagrelor
heart_failure_contraindicated = celecoxib | diclofenac_systemic | domperidon | dronedaron | eletriptan | etoricoxib \
                             | flecainid | methylphenidat | moxonidin | parecoxib | pioglitazon | tadalafil

file = open('atc_icd_excluded.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader, None)

codes = load_codes('ATC_Codes.csv')
data = []
for row in reader:
    data.append(dict(zip(headers, row)))
for sacubitril_valsartan_score in range(0, 101, 50):
    for aldosteronantagonist_score in range(0, 101, 50):
        for betablocker_score in range(0, 101, 50):
            for ivabradin_score in range(0, 101, 50):
                for dihydropyridin_score in range(0, 101, 50):
                    for herzglykosid_score in range(0, 101, 50):
                        for ace_hemmer_score in range(0, 101, 50):
                            for ass_score in range(0, 101, 50):
                                for p2y12_inhibitor_score in range(0, 101, 50):
                                    for schleifendiuretikum_score in range(0, 101, 50):
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

                                            if sacubitril_valsartan & atc_codes:
                                                score += sacubitril_valsartan_score

                                            if aldosteronantagonist & atc_codes:
                                                score += aldosteronantagonist_score
                                            if betablocker & atc_codes:
                                                score += betablocker_score

                                            if ivabradin & atc_codes:
                                                score += ivabradin_score

                                            if dihydropyridin & atc_codes:
                                                score += dihydropyridin_score

                                            if herzglykosid & atc_codes:
                                                score += herzglykosid_score

                                            if ace_hemmer & atc_codes:
                                                score += ace_hemmer_score
                                            if ass & atc_codes:
                                                score += ass_score
                                            if p2y12_inhibitor & atc_codes:
                                                score += p2y12_inhibitor_score

                                            if schleifendiuretikum & atc_codes:
                                                score += schleifendiuretikum_score

                                            if score >= 100 and any([is_chf(icd) for icd in row.values()]):
                                                true_positive += 1
                                            if score >= 100 and not any([is_chf(icd) for icd in row.values()]):
                                                false_positive += 1
                                            if score < 100 and not any([is_chf(icd) for icd in row.values()]):
                                                true_negative += 1
                                            if score < 100 and any([is_chf(icd) for icd in row.values()]):
                                                false_negative += 1

                                        original_stdout = sys.stdout  # Save a reference to the original standard output

                                        with open('CHF_result.txt', 'a') as f:

                                            print('Specificity:', true_negative / (true_negative + false_positive),
                                                  'Sensitivity:', true_positive / (true_positive + false_negative),
                                                  sacubitril_valsartan_score, aldosteronantagonist_score,
                                                  betablocker_score, ivabradin_score, dihydropyridin_score,
                                                  herzglykosid_score, ace_hemmer_score, ass_score, p2y12_inhibitor_score,
                                                  schleifendiuretikum_score, file=f)

                                            print('True Positives:', true_positive, 'True Negatives:', true_negative,
                                                  'False Positives:', false_positive,
                                                  'False Negatives:',
                                                  false_negative)  # validation: CAD(true) - true_positive = false_negative
                                            true_positive = 0
                                            true_negative = 0
                                            false_positive = 0
                                            false_negative = 0