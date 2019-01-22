generate_synthetic_data <- function(n,p,sigma){
  X <-matrix(rnorm(n*p),n)
  w <- matrix(rnorm(p),p)-0.5
  Y0 <- X %*% w
  temp <- matrix(rnorm(n,mean=0,sd=sigma))
  Y0 <- Y0 + temp
  
  Y <- matrix(rep(1,n),n)
  Y[Y0<0] = -1
}
