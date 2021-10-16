# generates decision_trees from train dataset
import csv

import numpy as np
from sklearn import tree, metrics

with open('cad_gold_standard_train.csv') as file:
    csv_reader = csv.reader(file, delimiter=';')

    # Header contains feature names
    row = next(csv_reader)
    feature_names = row[2:]

    # Load dataset, and target classes
    target_X, target_y = [], []
    for row in csv_reader:
        target_X.append(row[2:])
        target_y.append(row[1])  # target value

target_X = np.array(target_X)
target_y = np.array(target_y)


print(feature_names, target_X, target_y)

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_leaf=1)
clf = clf.fit(target_X, target_y)

y_pred = clf.predict(target_X)


print("Accuracy:{0:.5f}".format(metrics.accuracy_score(target_y, y_pred)), "\n")
print("Classification report")
print(metrics.classification_report(target_y, y_pred), "\n")
print("Confusion matrix")
print(metrics.confusion_matrix(target_y, y_pred), "\n")


dot_data = tree.export_graphviz(clf, out_file="tree.dot",
                                feature_names=feature_names,
                                class_names=['BO_positive', 'BO_negative'],
                                filled=True, rounded=True)


# dot -Tpng -Gdpi=600 tree.dot -o tree.png into the terminal; out_file="tree.dot" instead of None;

""" plot confusion matrix
sklearn.metrics.plot_confusion_matrix(clf, target_X, target_y, cmap=plt.cm.Blues)
plt.show()"""
