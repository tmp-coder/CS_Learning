% Predict the labels for a test set using logistic regression

function [yHat,numErrors] = LR_PredictLabels(XTest,yTest,wHat)

  % get dimensions
  [m,p] = size(XTest);
  
  % add a feature of 1's to XTrain
  XTest = [ones(m,1) XTest];
  
  % precompute X*w and exp(X*w)
  Xw = XTest*wHat;
  eXw = exp(Xw);
  
  % calculate p(Y=0)
  pY0 = 1./(1 + eXw);
  
  % calculate p(Y=1)
  pY1 = eXw./(1 + eXw);
  
  % choose best label
  [~,ind] = max([pY0,pY1],[],2);
  yHat = ind-1;
  
  % calculate error
  numErrors = sum(yHat != yTest);

end