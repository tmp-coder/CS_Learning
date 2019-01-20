import numpy as np
import matplotlib.pyplot as plt

beta_3_3 = 0.0333

def theta_MLE(theta,n,positive):
    return (theta ** positive)*((1 - theta) **(n-positive))


def theta_MAP(theta,n,positive):
    return theta_MLE(theta,n,positive) *(theta**2) * (1-theta) ** 2 / beta_3_3

def problem2():
    theta = np.linspace(0,1,endpoint= False)
    l_theta = theta_MLE(theta,n=10,positive=6)
    plt.plot(theta,l_theta,label = 'n=10,positive=6')
    plt.plot(theta, theta_MLE(theta,5,3),label ='n=5,positive=3')
    plt.plot(theta,theta_MLE(theta,100,60),label ='n=100,positive = 60')
    plt.legend()
    plt.show()

def problem3():
    theta = np.linspace(0,1,num=100,endpoint=False)
    y = theta_MAP(theta,10,6)
    plt.plot(theta,y,label = 'n=10,positive = 3')
    plt.plot(theta, theta_MAP(theta,5,3),label ='n=5,positive=3')
    plt.plot(theta,theta_MAP(theta,100,60),label ='n=100,positive = 60')
    
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # problem2()
    problem3()