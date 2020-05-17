def brute(n):
    for x in range(2, n): # Loops x from 2 to n-1
        if n % x == 0: # If x divides n evenly
            return False
    return True
