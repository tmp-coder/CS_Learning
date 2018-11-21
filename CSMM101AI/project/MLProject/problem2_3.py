import csv
import sys

import numpy as np
import pandas as pd
from sklearn import preprocessing


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


def gradient_descent(X_train, Y_train, alpha, num_of_iter=100):
    w = np.zeros(X_train.shape[1])
    b = 0
    num_of_trains = X_train.shape[0]
    for i in range(num_of_iter):
        diff = X_train.dot(w) + b - Y_train
        b -= diff.sum() / num_of_trains * alpha

        tmp_mat = (X_train.transpose() * diff).transpose()
        w -= alpha / num_of_trains * tmp_mat.sum(axis=0)

    return [b, w[0], w[1]]


def main():
    file_in = sys.argv[1]
    file_out = sys.argv[2]

    X_train, Y_train = read_data(file_in)
    X_train = preprocessing.scale(X_train)
    alpha = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 100]
    res = []
    for learn_rate in alpha:
        w = gradient_descent(X_train, Y_train, learn_rate)
        res.append([learn_rate, 100] + w)

    write_csv(res, file_out)


if __name__ == '__main__':
    main()
