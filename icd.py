from functools import cache


@cache
def is_chf(icd):
    # print(icd)
    if not icd:
        return False
    return icd.startswith('I11.0') \
        or icd.startswith('I13.0') \
        or icd.startswith('I13.2') \
        or icd.startswith('I50.0') \
        or icd.startswith('I50.1') \
        or icd == 'I50.9' \
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


@cache
def is_bronchial_obstruction(icd):
    if not icd:
        return False
    return icd.startswith('J45') \
        or icd.startswith('J44') \
        or icd.startswith('J46') \



"""
J44 Sonstige chronische obstruktive Lungenkrankheit
J45 Asthma bronchiale
J46 Status asthmaticus
"""
