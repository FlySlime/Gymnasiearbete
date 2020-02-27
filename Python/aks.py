import math

def isPerfectPower(n):
  for b in range(2, round(math.log2(n)) + 1):
    a = pow(n, 1 / b)
    if (a * 10) % 10 == 0:
      return True
  return False

def smallestR(n):
  max_k = math.floor(pow(math.log2(n), 2))
  next_r = True
  r = 2
  while next_r:
      next_r = False
      for k in range(1, max_k):
          if next_r:
              break

          if pow(n, k, r) == 1:
              next_r = 1
          elif pow(n, k, r) == 0:
              next_r = 0
      r += 1
  r -= 1
  return r

def checkDivisors(r, n):
  for a in range(2, min(r, n-1)+1, 1):
    if a % n == 0:
      return False
  return True

def totient(k):
  totatives = []
  for a in range(1, k+1):
    if math.gcd(k, a) == 1:
      totatives.append(a)
  return len(totatives)

def step5(n, r):
  for a in range(1, math.floor(math.sqrt(totient(r))*math.log(n, 2))):
    #this needs to be finished

def AKS(n):
  if isPerfectPower(n):
    return ("Composite")
  r = smallestR(n)
  if checkDivisors(r, n):
    return ("Composite")
  if n <= r:
    return ("Prime")
  #add step 5 here
