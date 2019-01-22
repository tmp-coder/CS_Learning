function [Y,X] = gen_synthetic_data(n,p,sigma)
    X = randn(n,p);
    w = rand(p,1) -0.5;
    Y0 = X * w + normrnd(0,sigma,n,1);
    Y = ones(n,1);
    Y(Y0<0) = -1;
end