#!/usr/bin/python3

"""Minimum operations"""

def minOperations(n):
    
    """Calculates the minimum number of operations needed to produce n H characters in the file."""
    
    if n <= 1:
        return 0
    
    count = 0
    i = 2
    
    while i <= n:
        if n % i == 0:
            count += i
            n //= i
        else:
            i += 1
            
    return count
