function [error] = ClassificationError(yHat, yTruth)
  error = sum(yHat != yTruth) / length(yTruth);
end

