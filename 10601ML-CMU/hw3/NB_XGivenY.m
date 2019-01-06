function [D] = NB_XGivenY(XTrain, yTrain)
  EconoRows = yTrain == 1;
  OnionRows = yTrain == 2;

  D = [(sum(XTrain(EconoRows,:), 1) .+ 1) / (sum(EconoRows) + 1) ;
       (sum(XTrain(OnionRows,:), 1) .+ 1) / (sum(OnionRows) + 1)];    
end

