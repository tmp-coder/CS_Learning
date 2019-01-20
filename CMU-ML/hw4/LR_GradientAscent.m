% Run the gradient ascent algorithm for logistic regression

function [wHat,objVals] = LR_GradientAscent(XTrain,yTrain)

    % Set the step size
    eta = .01;
    
    % Set the convergence tolerance
    tol = .001;
    
    % Get dimensions
    [n,p] = size(XTrain);
    
    % Initialize wHat
    wHat = zeros(p+1,1);
    
    % Initialize objVals
    objVals = LR_CalcObj(XTrain,yTrain,wHat);
    
    % Initialize convergence flag
    hasConverged = false;
    
    % Run gradient ascent until convergence
    while (~hasConverged)    
    
        % Calculate gradient
        grad = LR_CalcGrad(XTrain,yTrain,wHat);

        % Update parameter estimate
        wHat = LR_UpdateParams(wHat,grad,eta);

        % Calculate new objective
        newObj = LR_CalcObj(XTrain,yTrain,wHat);

        % Check convergence
        hasConverged = LR_CheckConvg(objVals(end),newObj,tol);

        % Store new objective
        objVals = [objVals ; newObj];        

    endwhile

end