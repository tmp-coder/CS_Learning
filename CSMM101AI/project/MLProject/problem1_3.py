import numpy as np
import matplotlib.pyplot as plt
import csv
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
        data = np.array(data,dtype=np.int32)
    return data[:, :2], data[:, 2:3].squeeze()


def perceptron(X, Y):
    update = True
    result = []
    w = np.zeros(X.shape[1],dtype=np.int32)
    b = 0
    while update:
        update = False
        for i in range(Y.size):
            y_hat = np.sign(np.sum(X[i] * w) + b)
            if y_hat * Y[i] <= 0:
                update = True
                b += Y[i]
                w += Y[i] * X[i]
        plot(X, Y, w,b)
        result.append([w[0], w[1], b])
    return result


def plot(X, Y, w,b):
    plt.scatter(X[:, 0], X[:, 1], c=Y)
    x = np.linspace(0, 14)
    y = (b - w[0] * x) / (w[1] + 1e-9)
    plt.plot(x, y)
    plt.pause(0.5)


def write_csv(data, file="output1.csv"):
    with open(file, "w") as f:
        writer = csv.writer(f)
        for d in data:
           # print(d)
            writer.writerow(d)


def main():
    file_in = sys.argv[1]
    file_out = sys.argv[2]

    X, Y = read_data(file_in)
    write_data = perceptron(X, Y)
    write_csv(write_data, file_out)


if __name__ == '__main__':
    main()
    plt.show()
