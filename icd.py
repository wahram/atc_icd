from functools import cache

@cache
def is_chf(icd):
    return icd.startswith('I11.0') \
           or icd.startswith('I13.0') \
           or icd.startswith('I50.0') \
           or icd.startswith('I50.1') \
           or icd == 'I50.9' \
           or icd == 'R57.0'

# @cache
# def is_cad und die anderen Krankheiten

