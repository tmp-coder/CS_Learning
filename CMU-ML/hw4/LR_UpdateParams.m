% Calculate the new value of wHat using the gradient 
% ascent update rule

function wHat = LR_UpdateParams(wHat,grad,eta)

  % update value of w
  wHat = wHat + eta.*grad;

end