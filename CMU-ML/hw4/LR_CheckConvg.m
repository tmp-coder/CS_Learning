% Check whether the objective value has converged 
% by comparing the difference between consecutive 
% objective values to the tolerance

function hasConverged = LR_CheckConvg(oldObj,newObj,tol)

  % compute difference between objectives
  diff = abs(oldObj-newObj);
  
  % compare difference to tolerance
  if (diff < tol)
    hasConverged = true;
  else
    hasConverged = false;
  endif

end