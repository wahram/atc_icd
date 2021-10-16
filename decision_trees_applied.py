# calculates performance of decision trees

import csv

import statsmodels.api as statsmodels

from atcs import *
from icd import *

bo_true_positive = 0
bo_true_negative = 0
bo_false_positive = 0
bo_false_negative = 0

chf_true_positive = 0
chf_true_negative = 0
chf_false_positive = 0
chf_false_negative = 0

cad_true_positive = 0
cad_true_negative = 0
cad_false_positive = 0
cad_false_negative = 0

epilepsy_true_positive = 0
epilepsy_true_negative = 0
epilepsy_false_positive = 0
epilepsy_false_negative = 0

gout_true_positive = 0
gout_true_negative = 0
gout_false_positive = 0
gout_false_negative = 0

gout_contraindications = 0
epilepsy_contraindications = 0
cad_contraindications = 0
chf_contraindications = 0
bo_contraindications = 0

highrisk_prescription_identified = 0

cad_contraindicated = celecoxib | etoricoxib | parecoxib | diclofenac | triptan | fludrocortison
bo_contraindicated = sotalol | dextrometorphan | carvedilol | metoprolol | propranolol | atenolol
gout_contraindicated = xipamid | hydrochlorothiazid | torasemid
chf_contraindicated = celecoxib | diclofenac | domperidon | dronedaron | eletriptan | etoricoxib \
                             | flecainid | methylphenidat | moxonidin | parecoxib | pioglitazon | tadalafil \
                             | cilostazol | desmopressin | fludrocortison
epilepsy_contraindicated = baclofen | bethanechol | buspiron | dimenhydrinat | diphenhydramin | doxylamin | \
                           levofloxacin | methocarbamol | metoclopramid | ofloxacin_oral | sulpirid | terizidon

file = open('test_1847_geputzt.csv')
reader = csv.reader(file, delimiter=';')
headers = next(reader)

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

# bronchial obstruction
    if any([is_r03al(atc) for atc in atc_codes]):
        if any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bo_true_positive += 1
            if bo_contraindicated & atc_codes:
                bo_contraindications += 1
        if not any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bo_false_positive += 1

    elif not any([is_r03al(atc) for atc in atc_codes]) and any([is_r03ak(atc) for atc in atc_codes]):
        if any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bo_true_positive += 1
            if bo_contraindicated & atc_codes:
                bo_contraindications += 1
        if not any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bo_false_positive += 1

    elif not any([is_r03al(atc) for atc in atc_codes]) and not any([is_r03ak(atc) for atc in atc_codes]) and any([is_r03bb(atc) for atc in atc_codes]):
        if any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bo_true_positive += 1
            if bo_contraindicated & atc_codes:
                bo_contraindications += 1
        if not any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bo_false_positive += 1

    else:
        if any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bo_false_negative += 1
        if not any([is_bronchial_obstruction(icd) for icd in icd_codes]):
            bo_true_negative += 1

# CHF
    if any([is_c03ca(atc) for atc in atc_codes]) and any([is_c03ba(atc) for atc in atc_codes]) and not any([is_b05bb(atc) for atc in atc_codes]):
        if any([is_chf(icd) for icd in icd_codes]):
            chf_true_positive += 1
            if chf_contraindicated & atc_codes:
                chf_contraindications += 1
        if not any([is_chf(icd) for icd in icd_codes]):
            chf_false_positive += 1

    elif any([is_c03ca(atc) for atc in atc_codes]) and not any([is_c03ba(atc) for atc in atc_codes]) and any([is_s01xa(atc) for atc in atc_codes]):
        if any([is_chf(icd) for icd in icd_codes]):
            chf_true_positive += 1
            if chf_contraindicated & atc_codes:
                chf_contraindications += 1
        if not any([is_chf(icd) for icd in icd_codes]):
            chf_false_positive += 1

    elif not any([is_c03ca(atc) for atc in atc_codes]) and any([is_a10bj(atc) for atc in atc_codes]):
        if any([is_chf(icd) for icd in icd_codes]):
            chf_true_positive += 1
            if chf_contraindicated & atc_codes:
                chf_contraindications += 1
        if not any([is_chf(icd) for icd in icd_codes]):
            chf_false_positive += 1

    elif not any([is_c03ca(atc) for atc in atc_codes]) and not any([is_a10bj(atc) for atc in atc_codes]) and any([is_m05bb(atc) for atc in atc_codes]):
        if any([is_chf(icd) for icd in icd_codes]):
            chf_true_positive += 1
            if chf_contraindicated & atc_codes:
                chf_contraindications += 1
        if not any([is_chf(icd) for icd in icd_codes]):
            chf_false_positive += 1

    else:
        if any([is_chf(icd) for icd in icd_codes]):
            chf_false_negative += 1
        if not any([is_chf(icd) for icd in icd_codes]):
            chf_true_negative += 1

# CAD
    if any([is_c10aa(atc) for atc in atc_codes]) and any([is_b01ac(atc) for atc in atc_codes]):
        if any([is_cad(icd) for icd in icd_codes]):
            cad_true_positive += 1
            if cad_contraindicated & atc_codes:
                cad_contraindications += 1
        if not any([is_cad(icd) for icd in icd_codes]):
            cad_false_positive += 1

    elif any([is_c10aa(atc) for atc in atc_codes]) and not any([is_b01ac(atc) for atc in atc_codes]) and any([is_n02ba(atc) for atc in atc_codes]):
        if any([is_cad(icd) for icd in icd_codes]):
            cad_true_positive += 1
            if cad_contraindicated & atc_codes:
                cad_contraindications += 1
        if not any([is_cad(icd) for icd in icd_codes]):
            cad_false_positive += 1

    elif not any([is_c10aa(atc) for atc in atc_codes]) and any([is_b01ac(atc) for atc in atc_codes]) and any([is_a10bh(atc) for atc in atc_codes]):
        if any([is_cad(icd) for icd in icd_codes]):
            cad_true_positive += 1
            if cad_contraindicated & atc_codes:
                cad_contraindications += 1
        if not any([is_cad(icd) for icd in icd_codes]):
            cad_false_positive += 1

    elif not any([is_c10aa(atc) for atc in atc_codes]) and not any([is_b01ac(atc) for atc in atc_codes]) and any([is_c01da(atc) for atc in atc_codes]):
        if any([is_cad(icd) for icd in icd_codes]):
            cad_true_positive += 1
            if cad_contraindicated & atc_codes:
                cad_contraindications += 1
        if not any([is_cad(icd) for icd in icd_codes]):
            cad_false_positive += 1

    else:
        if any([is_cad(icd) for icd in icd_codes]):
            cad_false_negative += 1
        if not any([is_cad(icd) for icd in icd_codes]):
            cad_true_negative += 1

# epilepsy
    if any([is_n03ax(atc) for atc in atc_codes]) and any([is_b01af(atc) for atc in atc_codes]) and any([is_m03bx(atc) for atc in atc_codes]):
        if any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_true_positive += 1
            if epilepsy_contraindicated & atc_codes:
                epilepsy_contraindications += 1
        if not any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_false_positive += 1

    elif any([is_n03ax(atc) for atc in atc_codes]) and not any([is_b01af(atc) for atc in atc_codes]) and any([is_n03ag(atc) for atc in atc_codes]):
        if any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_true_positive += 1
            if epilepsy_contraindicated & atc_codes:
                epilepsy_contraindications += 1
        if not any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_false_positive += 1

    elif not any([is_n03ax(atc) for atc in atc_codes]) and any([is_n03aa(atc) for atc in atc_codes]):
        if any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_true_positive += 1
            if epilepsy_contraindicated & atc_codes:
                epilepsy_contraindications += 1
        if not any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_false_positive += 1

    else:
        if any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_false_negative += 1
        if not any([is_epilepsy(icd) for icd in icd_codes]):
            epilepsy_true_negative += 1

# gout
    if any([is_m04aa(atc) for atc in atc_codes]):
        if any([is_gout(icd) for icd in icd_codes]):
            gout_true_positive += 1
            if gout_contraindicated & atc_codes:
                gout_contraindications += 1
        if not any([is_gout(icd) for icd in icd_codes]):
            gout_false_positive += 1

    elif not any([is_m04aa(atc) for atc in atc_codes]) and any([is_m04ac(atc) for atc in atc_codes]):
        if any([is_gout(icd) for icd in icd_codes]):
            gout_true_positive += 1
            if gout_contraindicated & atc_codes:
                gout_contraindications += 1
        if not any([is_gout(icd) for icd in icd_codes]):
            gout_false_positive += 1

    elif not any([is_m04aa(atc) for atc in atc_codes]) and not any([is_m04ac(atc) for atc in atc_codes]) and any([is_r06ax(atc) for atc in atc_codes]):
        if any([is_gout(icd) for icd in icd_codes]):
            gout_true_positive += 1
            if gout_contraindicated & atc_codes:
                gout_contraindications += 1
        if not any([is_gout(icd) for icd in icd_codes]):
            gout_false_positive += 1

    else:
        if any([is_gout(icd) for icd in icd_codes]):
            gout_false_negative += 1
        if not any([is_gout(icd) for icd in icd_codes]):
            gout_true_negative += 1


print('High risk prescriptions', highrisk_prescription_identified)
print('gout contraindications:', gout_contraindications)
print('epilepsy contraindications:', epilepsy_contraindications)
print('CAD contraindications:', cad_contraindications)
print('CHF contraindications:', chf_contraindications)
print('BO contraindications', bo_contraindications)

# BO
try:
    bo_specificity = bo_true_negative / (bo_true_negative + bo_false_positive)
except:
    bo_specificity = 1

try:
    bo_sensitivity = bo_true_positive / (bo_true_positive + bo_false_negative)
except:
    bo_sensitivity = 1

bo_ppv = bo_true_positive / (bo_true_positive + bo_false_positive)
bo_npv = bo_true_negative / (bo_true_negative + bo_false_negative)
print('BO_Specificity:', bo_specificity,
      statsmodels.stats.proportion_confint(bo_true_negative, bo_true_negative + bo_false_positive, alpha=0.05, method='wilson'))
print('BO_Sensitivity:', bo_sensitivity,
      statsmodels.stats.proportion_confint(bo_true_positive, bo_true_positive + bo_false_negative, alpha=0.05, method='wilson'))
print('BO_PPV:', bo_ppv,
      statsmodels.stats.proportion_confint(bo_true_positive, bo_true_positive + bo_false_positive, alpha=0.05, method='wilson'))
print('BO_NPV:', bo_npv,
      statsmodels.stats.proportion_confint(bo_true_negative, bo_true_negative + bo_false_negative, alpha=0.05, method='wilson'))

print('BO_True Positives:', bo_true_positive, 'BO_True Negatives:', bo_true_negative, 'BO_False Positives:', bo_false_positive,
      'BO_False Negatives:', bo_false_negative)  # validation: bronchial_obstruction(true) - true_positive = false_negative

bo_precision = bo_ppv
bo_recall = bo_sensitivity
print('BO_Precision:', bo_precision, 'BO_Recall:', bo_recall, 'BO_F1:', 2 * bo_precision * bo_recall / (bo_precision + bo_recall),
      'BO_Accuracy:', (bo_true_positive + bo_true_negative) / (bo_true_positive + bo_true_negative + bo_false_positive + bo_false_negative))

# CHF
try:
    chf_specificity = chf_true_negative / (chf_true_negative + chf_false_positive)
except:
    chf_specificity = 1

try:
    chf_sensitivity = chf_true_positive / (chf_true_positive + chf_false_negative)
except:
    chf_sensitivity = 1

chf_ppv = chf_true_positive / (chf_true_positive + chf_false_positive)
chf_npv = chf_true_negative / (chf_true_negative + chf_false_negative)

print('CHF_Specificity:', chf_specificity,
      statsmodels.stats.proportion_confint(chf_true_negative, chf_true_negative + chf_false_positive, alpha=0.05, method='wilson'))
print('CHF_Sensitivity:', chf_sensitivity,
      statsmodels.stats.proportion_confint(chf_true_positive, chf_true_positive + chf_false_negative, alpha=0.05, method='wilson'))
print('CHF_PPV:', chf_ppv,
      statsmodels.stats.proportion_confint(chf_true_positive, chf_true_positive + chf_false_positive, alpha=0.05, method='wilson'))
print('CHF_NPV:', chf_npv,
      statsmodels.stats.proportion_confint(chf_true_negative, chf_true_negative + chf_false_negative, alpha=0.05, method='wilson'))

print('CHF_True Positives:', chf_true_positive, 'CHF_True Negatives:', chf_true_negative, 'CHF_False Positives:', chf_false_positive,
      'CHF_False Negatives:', chf_false_negative)  # validation: CHF(true) - true_positive = false_negative

chf_precision = chf_ppv
chf_recall = chf_sensitivity
print('CHF_Precision:', chf_precision, 'CHF_Recall:', chf_recall, 'CHF_F1:', 2 * chf_precision * chf_recall / (chf_precision + chf_recall),
      'CHF_Accuracy:', (chf_true_positive + chf_true_negative) / (chf_true_positive + chf_true_negative + chf_false_positive + chf_false_negative))

# CAD
try:
    cad_specificity = cad_true_negative / (cad_true_negative + cad_false_positive)
except:
    cad_specificity = 1

try:
    cad_sensitivity = cad_true_positive / (cad_true_positive + cad_false_negative)
except:
    cad_sensitivity = 1

cad_ppv = cad_true_positive / (cad_true_positive + cad_false_positive)
cad_npv = cad_true_negative / (cad_true_negative + cad_false_negative)

print('CAD_Specificity:', cad_specificity,
      statsmodels.stats.proportion_confint(cad_true_negative, cad_true_negative + cad_false_positive, alpha=0.05, method='wilson'))
print('CAD_Sensitivity:', cad_sensitivity,
      statsmodels.stats.proportion_confint(cad_true_positive, cad_true_positive + cad_false_negative, alpha=0.05, method='wilson'))
print('CAD_PPV:', cad_ppv,
      statsmodels.stats.proportion_confint(cad_true_positive, cad_true_positive + cad_false_positive, alpha=0.05, method='wilson'))
print('CAD_NPV:', cad_npv,
      statsmodels.stats.proportion_confint(cad_true_negative, cad_true_negative + cad_false_negative, alpha=0.05, method='wilson'))

print('CAD_True Positives:', cad_true_positive, 'CAD_True Negatives:', cad_true_negative, 'CAD_False Positives:', cad_false_positive,
      'CAD_False Negatives:', cad_false_negative)  # validation: CAD(true) - true_positive = false_negative

cad_precision = cad_ppv
cad_recall = cad_sensitivity
print('CAD_Precision:', cad_precision, 'CAD_Recall:', cad_recall, 'CAD_F1:', 2 * cad_precision * cad_recall / (cad_precision + cad_recall),
      'CAD_Accuracy:', (cad_true_positive + cad_true_negative) / (cad_true_positive + cad_true_negative + cad_false_positive + cad_false_negative))

# Epilepsy
try:
    epilepsy_specificity = epilepsy_true_negative / (epilepsy_true_negative + epilepsy_false_positive)
except:
    epilepsy_specificity = 1

try:
    epilepsy_sensitivity = epilepsy_true_positive / (epilepsy_true_positive + epilepsy_false_negative)
except:
    epilepsy_sensitivity = 1

epilepsy_ppv = epilepsy_true_positive / (epilepsy_true_positive + epilepsy_false_positive)
epilepsy_npv = epilepsy_true_negative / (epilepsy_true_negative + epilepsy_false_negative)

print('Epilepsy_Specificity:', epilepsy_specificity,
      statsmodels.stats.proportion_confint(epilepsy_true_negative, epilepsy_true_negative + epilepsy_false_positive, alpha=0.05, method='wilson'))
print('Epilepsy_Sensitivity:', epilepsy_sensitivity,
      statsmodels.stats.proportion_confint(epilepsy_true_positive, epilepsy_true_positive + epilepsy_false_negative, alpha=0.05, method='wilson'))
print('Epilepsy_PPV:', epilepsy_ppv,
      statsmodels.stats.proportion_confint(epilepsy_true_positive, epilepsy_true_positive + epilepsy_false_positive, alpha=0.05, method='wilson'))
print('Epilepsy_NPV:', epilepsy_npv,
      statsmodels.stats.proportion_confint(epilepsy_true_negative, epilepsy_true_negative + epilepsy_false_negative, alpha=0.05, method='wilson'))

print('Epilepsy_True Positives:', epilepsy_true_positive, 'Epilepsy_True Negatives:', epilepsy_true_negative, 'Epilepsy_False Positives:', epilepsy_false_positive,
      'Epilepsy_False Negatives:', epilepsy_false_negative)  # validation: Epilepsy(true) - true_positive = false_negative

epilepsy_precision = epilepsy_ppv
epilepsy_recall = epilepsy_sensitivity
print('Epilepsy_Precision:', epilepsy_precision, 'Epilepsy_Recall:', epilepsy_recall, 'Epilepsy_F1:', 2 * epilepsy_precision * epilepsy_recall / (epilepsy_precision + epilepsy_recall),
      'Epilepsy_Accuracy:', (epilepsy_true_positive + epilepsy_true_negative) / (epilepsy_true_positive + epilepsy_true_negative + epilepsy_false_positive + epilepsy_false_negative))

# Gout
try:
    gout_specificity = gout_true_negative / (gout_true_negative + gout_false_positive)
except:
    gout_specificity = 1

try:
    gout_sensitivity = gout_true_positive / (gout_true_positive + gout_false_negative)
except:
    gout_sensitivity = 1

gout_ppv = gout_true_positive / (gout_true_positive + gout_false_positive)
gout_npv = gout_true_negative / (gout_true_negative + gout_false_negative)

print('Gout_Specificity:', gout_specificity,
      statsmodels.stats.proportion_confint(gout_true_negative, gout_true_negative + gout_false_positive, alpha=0.05, method='wilson'))
print('Gout_Sensitivity:', gout_sensitivity,
      statsmodels.stats.proportion_confint(gout_true_positive, gout_true_positive + gout_false_negative, alpha=0.05, method='wilson'))
print('Gout_PPV:', gout_ppv,
      statsmodels.stats.proportion_confint(gout_true_positive, gout_true_positive + gout_false_positive, alpha=0.05, method='wilson'))
print('Gout_NPV:', gout_npv,
      statsmodels.stats.proportion_confint(gout_true_negative, gout_true_negative + gout_false_negative, alpha=0.05, method='wilson'))

print('Gout_True Positives:', gout_true_positive, 'Gout_True Negatives:', gout_true_negative, 'Gout_False Positives:', gout_false_positive,
      'Gout_False Negatives:', gout_false_negative)  # validation: Gout(true) - true_positive = false_negative

gout_precision = gout_ppv
gout_recall = gout_sensitivity
print('Gout_Precision:', gout_precision, 'Gout_Recall:', gout_recall, 'Gout_F1:', 2 * gout_precision * gout_recall / (gout_precision + gout_recall),
      'Gout_Accuracy:', (gout_true_positive + gout_true_negative) / (gout_true_positive + gout_true_negative + gout_false_positive + gout_false_negative))
