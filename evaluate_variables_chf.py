# establish different specifity and sensitivity pairs with their variables for CHF algorithm
import csv
from atcs import *
import sys
from itertools import product
from cli import progress
from icd import is_chf

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

"""aldosteronantagonist = eplerenon | spironolacton
betablocker = metoprolol | bisoprolol | carvedilol | atenolol | nebivolol
dihydropyridin = amlodipin | nifedipin | felodipin | lercanidipin
herzglykosid = digoxin | digitoxin
ace_hemmer = captopril | enalapril | lisinopril | ramipril
at1_antagonist = losartan | valsartan | irbesartan | candesartan | telmisartan | olmesartan
hf_drug_without_herzglykosid = sacubitril_valsartan | eplerenon | betablocker | spironolacton | ivabradin | dihydropyridin | ace_hemmer
schleifendiuretikum = furosemid | torasemid
p2y12_inhibitor = clopidogrel | prasugrel | ticagrelor"""

file = open('atc_icd_inplausible_excluded.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader)

data = []
for row in reader:
    data.append(dict(zip(headers, row)))

params = list(product(
    [i for i in range(0, 101, 50)],  # sacubitril_valsartan
    [i for i in range(0, 101, 50)],  # aldosteronantagonist
    [i for i in range(0, 101, 50)],  # betablocker
    [i for i in range(0, 101, 50)],  # ivabradin
    [i for i in range(0, 101, 50)],  # dihydropyridin
    [i for i in range(0, 101, 50)],  # herzglykosid
    [i for i in range(0, 101, 50)],  # ace_hemmer
    [i for i in range(0, 101, 50)],  # at1_antagonist
    [i for i in range(0, 101, 50)],  # ass
    [i for i in range(0, 101, 50)],  # p2y12_inhibitor
    [i for i in range(0, 101, 50)]   # schleifendiuretikum
))

params_max = len(params)
cycle_counter = 0
for param in params:
    sacubitril_valsartan_score, aldosteronantagonist_score, betablocker_score, ivabradin_score, dihydropyridin_score, \
    herzglykosid_score, ace_hemmer_score, at1_antagonist_score, ass_score, p2y12_inhibitor_score, \
    schleifendiuretikum_score = param

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

        """if sacubitril_valsartan & atc_codes:
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

        if at1_antagonist & atc_codes:
            score += at1_antagonist_score

        if ass & atc_codes:
            score += ass_score

        if p2y12_inhibitor & atc_codes:
            score += p2y12_inhibitor_score

        if schleifendiuretikum & atc_codes:
            score += schleifendiuretikum_score"""

        if score >= 100 and any([is_chf(icd) for icd in icd_codes]):
            true_positive += 1
        if score >= 100 and not any([is_chf(icd) for icd in icd_codes]):
            false_positive += 1
        if score < 100 and not any([is_chf(icd) for icd in icd_codes]):
            true_negative += 1
        if score < 100 and any([is_chf(icd) for icd in icd_codes]):
            false_negative += 1

    original_stdout = sys.stdout  # Save a reference to the original standard output
    with open('CHF_result.txt', 'a') as f:
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
              sacubitril_valsartan_score, aldosteronantagonist_score,
              betablocker_score, ivabradin_score, dihydropyridin_score,
              herzglykosid_score, ace_hemmer_score, at1_antagonist_score, ass_score, p2y12_inhibitor_score,
              schleifendiuretikum_score, file=f)

        print('True Positives:', true_positive, 'True Negatives:', true_negative,
              'False Positives:', false_positive,
              'False Negatives:',
              false_negative)  # validation: CAD(true) - true_positive = false_negative
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
        progress(params_max, cycle_counter)