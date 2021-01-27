from functools import cache

@cache
def is_chf(icd):
    #print(icd)
    if not icd:
        return False
    return icd.startswith('I11.0') \
           or icd.startswith('I13.0') \
           or icd.startswith('I13.2') \
           or icd.startswith('I50.0') \
           or icd.startswith('I50.1') \
           or icd == 'I50.9' \
           or icd == 'R57.0'

@cache
def is_cad(icd):
    if not icd:
        return False
    try:
        return 19 < int(icd.split('.')[0][1:]) < 26
    except:
        print(icd)
        return False