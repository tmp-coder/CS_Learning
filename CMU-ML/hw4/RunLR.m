% Solution code to HW4, Problem 2

function RunLR()

  % Load data
  load HW4Data.mat

  % Train logistic regression
  [wHat,objVals] = LR_GradientAscent(XTrain,yTrain);

  % Test logistic regression
  [yHat,numErrors] = LR_PredictLabels(XTest,yTest,wHat);

  % Print the number of misclassified examples
  fprintf('There were %d misclassified examples in the test set\n',numErrors);

  % Plot the objective value per iteration
  h = figure; hold on;
  plot(objVals,'LineWidth',2);
  xlabel('Gradient Ascent Iteration','FontSize',14);
  ylabel('Logistic Regression Objective Value','FontSize',14);
  title('Convergence of Gradient Ascent for Logistic Regression','FontSize',14);
  fprintf('Gradient ascent coverges after %d iterations\n',length(objVals)-1);

  % Evaluate the training and test erorr as a function of training set size
  n = size(XTrain,1);
  kVals = 10:10:n;
  m = size(XTest,1);
  trainingError = zeros(length(kVals),1);
  testError = zeros(length(kVals),1);
  for kInd = 1:length(kVals)
    % Set k
    k = kVals(kInd);
    % Generate training set
    subsetInds = randperm(n,k);
    XTrainSubset = XTrain(subsetInds,:);
    yTrainSubset = yTrain(subsetInds);
    % Train logistic regression
    wHat = LR_GradientAscent(XTrainSubset,yTrainSubset);
    % Test classifier on training set
    [yHatTrain,numErrorsTrain] = LR_PredictLabels(XTrainSubset,yTrainSubset,wHat);
    trainingError(kInd) = numErrorsTrain/k;
    % Test classifier on test set
    [yHatTest,numErrorsTest] = LR_PredictLabels(XTest,yTest,wHat);
    testError(kInd) = numErrorsTest/m;    
  endfor
  h = figure; hold on;
  plot(kVals,trainingError,'b','LineWidth',2);
  plot(kVals,testError,'r','LineWidth',2);
  xlabel('Training Set Size','FontSize',14);
  ylabel('Prediction Error','FontSize',14);
  l = legend('Training Error','Test Error');
  title('Logistic Regression Performance by Training Set Size','FontSize',14);
  
  % Perform the same experiment but average over multiple random training sets
  n = size(XTrain,1);
  kVals = 10:10:n;
  m = size(XTest,1);
  trainingError = zeros(length(kVals),1);
  testError = zeros(length(kVals),1);
  for kInd = 1:length(kVals)
    % Set k
    k = kVals(kInd);
    for rep = 1:100
      % Generate training set
      subsetInds = randperm(n,k);
      XTrainSubset = XTrain(subsetInds,:);
      yTrainSubset = yTrain(subsetInds);
      % Train logistic regression
      wHat = LR_GradientAscent(XTrainSubset,yTrainSubset);
      % Test classifier on training set
      [yHatTrain,numErrorsTrain] = LR_PredictLabels(XTrainSubset,yTrainSubset,wHat);
      trainingError(kInd) += numErrorsTrain/k;
      % Test classifier on test set
      [yHatTest,numErrorsTest] = LR_PredictLabels(XTest,yTest,wHat);
      testError(kInd) += numErrorsTest/m;
    end
    trainingError(kInd) /= 100;
    testError(kInd) /= 100;
  endfor
  h = figure; hold on;
  plot(kVals,trainingError,'b','LineWidth',2);
  plot(kVals,testError,'r','LineWidth',2);
  xlabel('Training Set Size','FontSize',14);
  ylabel('Average Prediction Error','FontSize',14);
  l = legend('Training Error','Test Error');
  title('Average Logistic Regression Performance by Training Set Size','FontSize',14);

end