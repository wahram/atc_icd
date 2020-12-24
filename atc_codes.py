# atc codes helper function
def load_codes(file_name):
    file = open(file_name)

    codes = {}
    for row in file:
        code = row.strip().split("\t", 1)
        codes[code[0]] = code[1] if len(code) > 1 else code[0]

    return codes