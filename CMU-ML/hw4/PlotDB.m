% Solution to HW4, Problem 2, extra credit

function PlotDB()

  % Load data
  load HW4Data.mat

  % Train logistic regression
  [wHat,objVals] = LR_GradientAscent(XTrain,yTrain);

  % Plot data in 2d
  h = figure; hold on;
  j = 1; k = 2;
  ind0 = yTest == 0;
  ind1 = yTest == 1;
  plot(XTest(ind0,j),XTest(ind0,k),'r.');
  plot(XTest(ind1,j),XTest(ind1,k),'b.');
  
  % Calculate decision boundary
  dbDimJ = min(XTest(:,j)):.01:max(XTest(:,j));
  dbDimK = -(wHat(1) + wHat(j+1).*dbDimJ)./wHat(k+1);
  
  % Plot decision boundary
  plot(dbDimJ,dbDimK,'k-','LineWidth',2);
  
  % Set plot title and axis labels
  xlabel(sprintf('Dimension %d',j),'FontSize',14);
  ylabel(sprintf('Dimension %d',k),'FontSize',14);
  title('Logistic Regression Decision Boundary','FontSize',14);
  
end