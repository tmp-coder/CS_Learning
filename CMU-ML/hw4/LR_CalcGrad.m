% Calculate the gradient of the logistic regression
% objective function with respect to each parameter

function grad = LR_CalcGrad(XTrain,yTrain,wHat)

  % get dimensions
  [n,p] = size(XTrain);

  % add a feature of 1's to XTrain
  XTrain = [ones(n,1) XTrain];
  
  % precompute X*w and exp(X*w)
  Xw = XTrain*wHat;
  eXw = exp(Xw);  

  % calculate gradient
  grad = sum(repmat(yTrain,1,p+1).*XTrain - XTrain.*repmat(eXw./(1+eXw),1,p+1))';

end