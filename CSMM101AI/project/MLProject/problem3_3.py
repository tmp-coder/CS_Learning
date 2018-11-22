import csv
import sys

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def read_data(csv_input):
    """
    return [x,y]
    :param csv_input:
    :return:
    """
    X = pd.read_csv(csv_input)
    X = np.array(X)
    return X[:, :2], X[:, -1]


def write_csv(data, file="output1.csv"):
    with open(file, "w") as f:
        writer = csv.writer(f)
        for d in data:
            # print(d)
            writer.writerow(d)

def candidate_model():
    """
    return the model and grid search para the project used
    :return:
    """
    ret = []

    # svm_linear
    svm_linear = svm.SVC()
    linear_svm_para = {
        "C" :[0.1, 0.5, 1, 5, 10, 50, 100],
        "kernel": ['linear']
    }
    ret.append(['svm_linear',svm_linear, linear_svm_para])

    # svm_polynomial

    svm_polynomial = svm.SVC()
    svm_polynomial_para = {
        "C": [0.1,1,3],
        "degree": [4,5,6],
        "gamma": [0.1,0.5],
        "kernel":['poly']
    }
    ret.append(['svm_polynomial',svm_polynomial,svm_polynomial_para])

    # svm_rbf
    svm_rbf = svm.SVC()
    svm_rbf_para = {
        "C": [0.1, 0.5, 1, 5, 10, 50, 100],
        "gamma": [0.1, 0.5, 1, 3, 6, 10],
        "kernel": ['rbf']
    }
    ret.append(["svm_rbf",svm_rbf, svm_rbf_para])

    # logistic
    logistic = LogisticRegression()
    logistic_para = {
        "C": [0.1, 0.5, 1, 5, 10, 50, 100]
    }
    ret.append(["logistic", logistic,logistic_para])

    # knn
    knn = KNeighborsClassifier()
    knn_para = {
        "n_neighbors": list(range(1,51)),
        "leaf_size": list(range(5,61,5))
    }
    ret.append(["knn", knn, knn_para])


    # decision_tree
    decision_tree = DecisionTreeClassifier()
    dc_tree_para = {
        "max_depth": list(range(1,51)),
        "min_samples_split": list(range(2,11))
    }
    ret.append(["decision_tree",decision_tree,dc_tree_para])

    # random_forest
    random_forest = RandomForestClassifier()
    random_forest_para = {
        "max_depth": list(range(1,51)),
        "min_samples_split": list(range(2, 11))
    }
    ret.append(["random_forest", random_forest,random_forest_para])

    return ret

def main():
    file_in = sys.argv[1]
    file_out = sys.argv[2]

    X_raw, Y_raw = read_data(file_in)
    X_train, X_test, Y_train, Y_test = train_test_split(X_raw, Y_raw, stratify=Y_raw, test_size=0.4)
    # code from stackOverFlow : https://stackoverflow.com/questions/29438265/stratified-train-test-split-in-scikit-learn

    cvfold = 5 # 5 fold cv

    models = candidate_model()

    res =[]

    # main logic

    for m in models:
        best_model = GridSearchCV(m[1],m[2],cv=cvfold)
        best_model.fit(X_train,Y_train)
        res.append([m[0],"%0.9f" % best_model.best_score_, "%0.9f" % best_model.score(X_test,Y_test)])

    write_csv(res, file_out)


if __name__ == '__main__':
    main()
