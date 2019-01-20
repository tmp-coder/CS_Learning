from scipy.io import loadmat
import numpy as np

mat_file_name = "HW3Data.mat"
data_name = ['Vocabulary', 'XTrain', 'yTrain', 'XTest', 'yTest', 'XTrainSmall','yTrainSmall']
eps = 1e-9
def data_preprocess(file_name):
    data = loadmat(file_name)
    return [data[e] for e in data_name]

Vocabulary, XTrain, yTrain, XTest, yTest, XTrainSmall,yTrainSmall = data_preprocess(mat_file_name)

def logProd(x):
    return x.sum(1)

def XgivenY(XTrain,YTrain):
    """
    return : a 2*V matrix represent P(X_w=1|Y=y) with a prior beta(beta[i]) distribution
    """
    yTrain = YTrain.squeeze()
    Erows = yTrain==1
    Orows = yTrain==2
    return np.row_stack(((XTrain[Erows].sum(0)+1)/(Erows.sum()+1),
    (XTrain[Orows].sum(0)+1)/(Orows.sum()+1)))

def YPrior_Eco(YTrain):
    """
    return P(Y==1) with MLE
    """
    yTrain = YTrain.squeeze()
    return np.sum(YTrain==1) / yTrain.size

def classify(D,p,XTest):
    D = np.asarray(D)
    XTest = XTest.toarray()
    pos_prob = D[0,:]*XTest + (1-D[0,:]) * (1-XTest)
    neg_prob = D[1,:] * XTest+(1-D[1,:]) * ( 1 - XTest)
    pos_prob = logProd(np.log(pos_prob+eps)) + np.log(p+eps)
    neg_prob = logProd(np.log(neg_prob + eps)) + np.log(1-p + eps)
    return np.argmax(np.column_stack((pos_prob,neg_prob)),axis=1) + 1

def classificationErr(y_true,y_hat):
    y_true = y_true.squeeze()
    y_hat = y_hat.squeeze()
    return 1 - np.sum(y_true == y_hat) / y_hat.size

def model_err(XTrain,YTrain):
    D = XgivenY(XTrain,YTrain)
    p = YPrior_Eco(YTrain)
    yhat_train = classify(D,p,XTrain)
    yhat_test = classify(D,p,XTest)
    train_err = classificationErr(YTrain,yhat_train)
    test_err = classificationErr(yhat_test,yTest)
    print("train err = ",train_err,"test err = ",test_err)


def problem_g():
    model_err(XTrain,yTrain)

def problem_h():
    model_err(XTrainSmall,yTrainSmall)

    
