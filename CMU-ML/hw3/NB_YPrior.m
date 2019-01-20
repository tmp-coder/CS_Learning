function [p] = NB_YPrior(yTrain)
  p = sum(yTrain == 1) / length(yTrain);
end

