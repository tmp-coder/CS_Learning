import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
import time


def read_data(csv_input):
    """
    return [x,y]
    :param csv_input:
    :return:
    """
    data = None
    with open(csv_input, "r") as csvFile:
        data = [list(map(int, _)) for _ in csv.reader(csvFile)]
        data = np.array(data, dtype=np.int32)
    return data[:, :2], data[:, -1]


def perceptron(X, Y, isplot = False):

    update = True
    result = []
    w = np.zeros(X.shape[1], dtype=np.int32)
    b = 0
    # print(Y)
    while update:
        update = False
        for i in range(Y.size):
            y_hat = np.sign(np.sum(X[i] * w) + b)
            if y_hat * Y[i] <= 0:
                update = True
                b += Y[i]
                w += Y[i] * X[i]
        result.append([w[0], w[1], b])
    if isplot:

        plot(X,Y,result)

    return result


def plot(X, Y,res):
    plt.scatter(X[:, 0], X[:, 1], c=Y)
    # last fig
    plt.pause(0.5)

    x = np.linspace(0,14)
    y = (-res[-1][2] - res[-1][0] * x)/ (res[-1][1] + 1e-9)
    plt.plot(x,y)
    plt.pause(2)
    for w in res:
        x = np.linspace(0, 14)
        y = (-w[2] - w[0] * x) / (w[1] + 1e-9)
        plt.plot(x, y)
        plt.pause(0.5)
    plt.show()


def write_csv(data, file="output1.csv"):
    with open(file, "w") as f:
        writer = csv.writer(f)
        for d in data:
            # print(d)
            writer.writerow(d)


def main(isdebug = False):
    file_in = sys.argv[1]
    file_out = sys.argv[2]

    X, Y = read_data(file_in)
    write_data = perceptron(X, Y,isdebug)
    write_csv(write_data, file_out)


if __name__ == '__main__':
    main(False)
