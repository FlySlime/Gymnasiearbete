def lehmer(n):
  s = 4
  M = 2**n - 1
  for i in range(n-2):
    s = (s*s - 2) % M
  if s == 0:
    return True
  else:
    return False

print(lehmer(86243))
