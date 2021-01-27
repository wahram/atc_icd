# calculates probability for having heart failure
from atc_codes import load_codes
import csv
from atcs import *
from icd import is_chf

threshold = 100

highrisk_prescription_identified = 0
hf_unlikely = 0
hf_possible = 0
hf_probable = 0
hf_positive = 0

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

aldosteronantagonist = eplerenon | spironolacton
betablocker = metoprolol | bisoprolol | carvedilol | atenolol | nebivolol
dihydropyridin = amlodipin | nifedipin | felodipin | lercanidipin
herzglykosid = digoxin | digitoxin
ace_hemmer = captopril | enalapril | lisinopril | ramipril
hf_drug_without_herzglykosid = sacubitril_valsartan | eplerenon | betablocker | spironolacton | ivabradin | dihydropyridin | ace_hemmer
p2y12_inhibitor = clopidogrel | prasugrel | ticagrelor
schleifendiuretikum = furosemid | torasemid
at1_antagonist = at1_antagonist = losartan | valsartan | irbesartan | candesartan | telmisartan | olmesartan

heart_failure_contraindicated = celecoxib | diclofenac_systemic | domperidon | dronedaron | eletriptan | etoricoxib \
                             | flecainid | methylphenidat | moxonidin | parecoxib | pioglitazon | tadalafil

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
    for pos in range(1, 25 + 1):
        row_name = 'atc_%02d' % pos
        if row[row_name]:
            atc_codes.add(row[row_name])

    icd_codes = set()
    for pos in range(1, 20 + 1):
        row_name = 'icd10_%02d' % pos
        if row[row_name]:
            icd_codes.add(row[row_name])

    if sacubitril_valsartan & atc_codes:
        score += 100

    if aldosteronantagonist & atc_codes and betablocker & atc_codes:
        score += 100
    elif aldosteronantagonist & atc_codes:
        score += 90

    if ivabradin & atc_codes and (betablocker & atc_codes or dihydropyridin & atc_codes):
        score += 100
    elif ivabradin & atc_codes:
        score += 95

    if herzglykosid & atc_codes and len(hf_drug_without_herzglykosid & atc_codes) >= 2:
        score += 100
    elif herzglykosid & atc_codes and hf_drug_without_herzglykosid & atc_codes:
        score += 50

    if ace_hemmer & atc_codes and betablocker & atc_codes and (ass & atc_codes or p2y12_inhibitor & atc_codes):
        score += 90

    if schleifendiuretikum & atc_codes:
        score += 70




    if score == 0:
        hf_unlikely += 1
    elif score <= 50:
        hf_possible += 1
    elif score < 100:
        hf_probable += 1
    else:
        hf_positive += 1


    if score >= threshold and any([is_chf(icd) for icd in icd_codes]):
        true_positive += 1
        if heart_failure_contraindicated & atc_codes:
            highrisk_prescription_identified +=1
            #print(row)
    if score >= threshold and not any([is_chf(icd) for icd in icd_codes]):
        false_positive += 1
        #print(row)
        if heart_failure_contraindicated & atc_codes:
            highrisk_prescription_identified +=1
    if score < threshold and not any([is_chf(icd) for icd in icd_codes]):
        true_negative += 1
    if score < threshold and any([is_chf(icd) for icd in icd_codes]):
        false_negative += 1
        #print(row)

print('HF unlikely:', hf_unlikely, 'HF possible:', hf_possible, 'HF probable:', hf_probable, 'HF positive:', hf_positive)
print('True Positives:', true_positive, 'True Negatives:', true_negative, 'False Positives:', false_positive, 'False Negatives:', false_negative) # validation: HF(true) - true_positive = false_negative
print('alpha-error:', false_positive / (false_positive + true_negative), 'beta-error:', false_negative / (false_negative + true_positive))  # alpha and beta error
print('Specificity:', true_negative / (true_negative + false_positive)) # identify healthy person
print('Sensitivity:', true_positive / (true_positive + false_negative)) # identify ill person
print('PPV:', true_positive / (true_positive + false_positive))
print('NPV:', true_negative / (true_negative + false_negative))
print('FDR:', false_positive / (true_positive + false_positive))
print('Precision:', true_positive / (true_positive + false_positive))
print('Recall:', true_positive / (true_positive + false_negative))
print('Positive:', true_positive + false_negative)
print('Negative:', true_negative + false_positive)

print(highrisk_prescription_identified)