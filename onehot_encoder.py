# one hot encodes csv. Headers in csv show all possible ATCs in the whole dataset.
import csv
import numpy as np

number_of_patients = 3506

np.set_printoptions(threshold=np.inf)

file = open('KHK_gold_standard Kopie.csv', encoding='utf-8-sig')
reader = csv.reader(file, delimiter=';')
headers = next(reader)
mapping = dict()

i = 0
for header in headers:
    mapping[header] = i
    i += 1

data = np.zeros((number_of_patients, len(headers)))

i = 0
for row in reader:
    for item in row:
        if not item:
            continue
        data[i, mapping[item]] = 1
    i += 1

np.savetxt('output.csv', data, fmt="%d", delimiter=";")
