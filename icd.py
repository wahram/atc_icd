from functools import cache


@cache
def is_chf(icd):
    # print(icd)
    if not icd:
        return False
    return icd.startswith('I11.0') \
        or icd.startswith('I13.0') \
        or icd.startswith('I13.2') \
        or icd.startswith('I50') \
        or icd == 'R57.0'


"""
I11.0- 	Hypertensive Herzkrankheit mit (kongestiver) Herzinsuffizienz
I13.0- 	Hypertensive Herz- und Nierenkrankheit mit (kongestiver) Herzinsuffizienz
I50.0- 	Rechtsherzinsuffizienz
I50.1- 	Linksherzinsuffizienz
I50.9 	Herzinsuffizienz, nicht näher bezeichnet
R57.0 	Kardiogener Schock
"""


@cache
def is_cad(icd):
    if not icd:
        return False
    return icd.startswith('I20') \
        or icd.startswith('I21') \
        or icd.startswith('I22') \
        or icd.startswith('I23') \
        or icd.startswith('I24') \
        or icd.startswith('I25')


# I20-I25 Ischämische Herzkrankheiten

@cache
def is_epilepsy(icd):
    if not icd:
        return False
    return icd.startswith('G40') \
        or icd.startswith('G41')

# G40 Epilepsie
# G41 Status epilepticus


@cache
def is_bipolar(icd):
    if not icd:
        return False
    return icd.startswith('F31')


# F31 Bipolare affektive Störung

@cache
def is_gout(icd):
    if not icd:
        return False
    return icd.startswith('M10') \
        or icd == 'E79.0'


# M10 Gicht
# E79.0 Hyperurikämie ohne Zeichen von entzündlicher Arthritis oder tophischer Gicht


@cache
def is_bronchial_obstruction(icd):
    if not icd:
        return False
    return icd.startswith('J44') \
        or icd.startswith('J45') \
        or icd.startswith('J46') \



"""
J44 Sonstige chronische obstruktive Lungenkrankheit
J45 Asthma bronchiale
J46 Status asthmaticus
"""

def is_c10aa(atc):
    if not atc:
        return False
    return atc.startswith('C10AA')  # HMG CoA reductase inhibitors


def is_n02ba(atc):
    if not atc:
        return False
    return atc.startswith('N02BA')  # Salicylic acid and derivatives


def is_b01ac(atc):
    if not atc:
        return False
    return atc.startswith('B01AC')  # Platelet aggregation inhibitors excl. heparin


def is_c01da(atc):
    if not atc:
        return False
    return atc.startswith('C01DA')  # Organic nitrates

# C10AA HMG CoA reductase inhibitors
# N02BA Salicylic acid and derivatives
# C07AB Beta blocking agents, selective
# B01AC Platelet aggregation inhibitors excl. heparin
# C01DA Organic nitrates

# R03BB Anticholinergics
# M05BB Bisphosphonates, combinations
# R03AL Adrenergics in combination with anticholinergics incl. triple combinations with corticosteroids
# A06AB Contact laxatives
# C05AA Corticosteroids
# R03AL Adrenergics in combination with anticholinergics incl. triple combinations with corticosteroids
# B05BB Solutions affecting the electrolyte balance
# R03AK Adrenergics in combination with corticosteroids or other drugs, excl. anticholinergics

# C03CA Sulfonamides, plain
# C03DA Aldosterone antagonists
# M04AA Preparations inhibiting uric acid production
# C03AA Thiazides, plain
# G04BE Drugs used in erectile dysfunction
# A02AA Magnesium compounds

# N03AX Other antiepileptics
# N02AA Natural opium alkaloids
# M03BX Other centrally acting agents
# A11DA Vitamin B1, plain
# J01EA Trimethoprim and derivatives

# H03BB Sulfur-containing imidazole derivatives
# A10AB Insulins and analogues for injection, fast-acting
# C04AD Purine derivatives
