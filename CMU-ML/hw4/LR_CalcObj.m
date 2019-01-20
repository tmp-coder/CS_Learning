% Calculate the logistic regression objective value

function obj = LR_CalcObj(XTrain,yTrain,wHat)

  % get dimensions
  [n,p] = size(XTrain);
  
  % add a feature of 1's to XTrain
  XTrain = [ones(n,1) XTrain];
  
  % precompute X*w and exp(X*w)
  Xw = XTrain*wHat;
  eXw = exp(Xw);
  
  % calculate objective value
  obj = sum(yTrain.*Xw - log(1 + eXw));
  
end