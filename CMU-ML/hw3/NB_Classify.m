function [yHat] = NB_Classify(D, p, XTest)
  m = size(XTest, 1);
  yHat = zeros(m, 1);

  for i = 1:m
    econo_probs = D(1,:) .* XTest(i,:) + (1 - D(1,:)) .* (1 - XTest(i,:));
    onion_probs = D(2,:) .* XTest(i,:) + (1 - D(2,:)) .* (1 - XTest(i,:));

    econo_score = logProd([log(econo_probs), log(p)]);
    onion_score = logProd([log(onion_probs), log(1-p)]);
    
    if econo_score > onion_score
      yHat(i) = 1;
    else
      yHat(i) = 2;
    end
  end
end

