

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

def is_epilepsy(icd):
    if not icd:
        return False
    return icd.startswith('G40') \
           or icd.startswith('G41')


# G40 Epilepsie
# G41 Status epilepticus


def is_bipolar(icd):
    if not icd:
        return False
    return icd.startswith('F31')


# F31 Bipolare affektive Störung

def is_gout(icd):
    if not icd:
        return False
    return icd.startswith('M10') \
           or icd == 'E79.0'


# M10 Gicht
# E79.0 Hyperurikämie ohne Zeichen von entzündlicher Arthritis oder tophischer Gicht


def is_bronchial_obstruction(icd):
    if not icd:
        return False
    return icd.startswith('J44') \
        or icd.startswith('J45') \
        or icd.startswith('J46')


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


def is_m04aa(atc):
    if not atc:
        return False
    return atc.startswith('M04AA')  # Preparations inhibiting uric acid production


def is_n03ax(atc):
    if not atc:
        return False
    return atc.startswith('N03AX')  # N03AX Other antiepileptics


def is_n02aa(atc):
    if not atc:
        return False
    return atc.startswith('N02AA')  # N02AA Natural opium alkaloids


def is_a11da(atc):
    if not atc:
        return False
    return atc.startswith('A11DA')  # A11DA Vitamin B1, plain


def is_m03bx(atc):
    if not atc:
        return False
    return atc.startswith('M03BX')  # M03BX Other centrally acting agents


def is_g04be(atc):
    if not atc:
        return False
    return atc.startswith('G04BE')  # G04BE Drugs used in erectile dysfunction


def is_j01ea(atc):
    if not atc:
        return False
    return atc.startswith('J01EA')  # J01EA Trimethoprim and derivatives


def is_c03ca(atc):
    if not atc:
        return False
    return atc.startswith('C03CA')  # C03CA Sulfonamides, plain


def is_c03da(atc):
    if not atc:
        return False
    return atc.startswith('C03DA')  # C03DA Aldosterone antagonists


def is_c03aa(atc):
    if not atc:
        return False
    return atc.startswith('C03AA')  # C03AA Thiazides, plain


def is_a02aa(atc):
    if not atc:
        return False
    return atc.startswith('A02AA')  # A02AA Magnesium compounds


def is_r03bb(atc):
    if not atc:
        return False
    return atc.startswith('R03BB')  # R03BB Anticholinergics


def is_m05bb(atc):
    if not atc:
        return False
    return atc.startswith('M05BB')  # M05BB Bisphosphonates, combinations


def is_r03al(atc):
    if not atc:
        return False
    return atc.startswith(
        'R03AL')  # R03AL Adrenergics in combination with anticholinergics incl. triple combinations with corticosteroids


def is_b05bb(atc):
    if not atc:
        return False
    return atc.startswith('B05BB')  # B05BB Solutions affecting the electrolyte balance


def is_b03ba(atc):
    if not atc:
        return False
    return atc.startswith('B03BA')  # B03BA Vitamin B12 (cyanocobalamin and analogues)


def is_g04ca(atc):
    if not atc:
        return False
    return atc.startswith('G04CA')  # G04CA Alpha-adrenoreceptor antagonists


def is_n03af(atc):
    if not atc:
        return False
    return atc.startswith('N03AF')  # N03AF Carboxamide derivatives


def is_n03ag(atc):
    if not atc:
        return False
    return atc.startswith('N03AG')  # N03AG Fatty acid derivatives


def is_c07ab(atc):
    if not atc:
        return False
    return atc.startswith('C07AB')  # C07AB Beta blocking agents, selective


def is_a10ae(atc):
    if not atc:
        return False
    return atc.startswith('A10AE')  # A10AE Insulins and analogues for injection, long-acting


def is_m01ah(atc):
    if not atc:
        return False
    return atc.startswith('M01AH')  # M01AH Coxibs


def is_c01dx(atc):
    if not atc:
        return False
    return atc.startswith('C01DX')  # C01DX Other vasodilators used in cardiac diseases


def is_s01ed(atc):
    if not atc:
        return False
    return atc.startswith('S01ED')  # S01ED Beta blocking agents


def is_r03ak(atc):
    if not atc:
        return False
    return atc.startswith('R03AK')  # R03AK Adrenergics in combination with corticosteroids or other drugs, excl. anticholinergics


def is_n02ab(atc):
    if not atc:
        return False
    return atc.startswith('N02AB')  # N02AB Phenylpiperidine derivatives


def is_a10ac(atc):
    if not atc:
        return False
    return atc.startswith('A10AC')  # A10AC Insulins and analogues for injection, intermediate-acting


def is_c03ba(atc):
    if not atc:
        return False
    return atc.startswith('C03BA')  # C03BA Sulfonamides, plain


def is_b05ba(atc):
    if not atc:
        return False
    return atc.startswith('B05BA')  # B05BA Solutions for parenteral nutrition

