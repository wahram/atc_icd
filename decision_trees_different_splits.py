# create decision_trees with different train/test splits
import csv

import numpy as np
import sklearn
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree, metrics
import graphviz

with open('bronchial_obstruction_gold_standard_deleted.csv') as file:
    csv_reader = csv.reader(file, delimiter=';')

    # Header contains feature names
    row = next(csv_reader)
    feature_names = row[2:]

    # Load dataset, and target classes
    khk_X, khk_y = [], []
    for row in csv_reader:
        khk_X.append(row[2:])
        khk_y.append(row[1])  # target value KHK

khk_X = np.array(khk_X)
khk_y = np.array(khk_y)


# print(feature_names, khk_X, khk_y)
for i in np.arange(0.1, 1.0, 0.1):
    X_train, X_test, y_train, y_test = train_test_split(khk_X, khk_y, train_size=i, random_state=0)

    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_leaf=1)
    clf = clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    print("Confusion matrix")
    print(metrics.confusion_matrix(y_test, y_pred), "\n")

    '''
    print("Confusion matrix train cohort")
    z_pred = clf.predict(X_train)
    print(metrics.confusion_matrix(y_train, z_pred), "\n")
    
    sklearn.metrics.plot_confusion_matrix(clf, X_test, y_test, cmap=plt.cm.Blues,)
    plt.show()
    
    
    dot_data = tree.export_graphviz(clf, out_file=None,
                                    feature_names=feature_names,
                                    class_names=['gout_positive', 'gout_negative'],
                                    filled=True, rounded=True)
    graph = graphviz.Source(dot_data)
    graph.render("image")
    '''
