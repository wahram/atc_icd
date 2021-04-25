# create decision_trees
import csv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree, metrics
import graphviz

with open('KHK_gold_standard.csv') as file:
    csv_reader = csv.reader(file, delimiter=';')

    # Header contains feature names
    row = next(csv_reader)
    feature_names = row[1:8]

    # Load dataset, and target classes
    khk_X, khk_y = [], []
    for row in csv_reader:
        khk_X.append(row[1:8])
        khk_y.append(row[8])  # target value KHK

khk_X = np.array(khk_X)
khk_y = np.array(khk_y)

print(feature_names, khk_X, khk_y)

X_train, X_test, y_train, y_test = train_test_split(khk_X, khk_y, test_size=0.95, random_state=0)

clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Accuracy:{0:.3f}".format(metrics.accuracy_score(y_test, y_pred)), "\n")
print("Classification report")
print(metrics.classification_report(y_test, y_pred), "\n")
print("Confusion matrix")
print(metrics.confusion_matrix(y_test, y_pred), "\n")

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=300)

tree.plot_tree(clf,
               feature_names=feature_names,
               class_names=['KHK_negativ', 'KHK-positiv'],
               filled=True)

fig.savefig('imagename.png')

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=feature_names,
                                class_names=['KHK_negativ', 'KHK-positiv'],
                                filled=True, rounded=True)
graph = graphviz.Source(dot_data)
graph.render("output")
