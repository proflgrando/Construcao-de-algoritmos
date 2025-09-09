def cumsum(x):
  if x < 0:
    return 0
  else:
    return x + cumsum(x - 1)

cumsum(5)
