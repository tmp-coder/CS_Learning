for {
  i <- 1 until 10
  j <- 1 until i
  if ((i + j) % 2 == 0)
} yield (i,j)