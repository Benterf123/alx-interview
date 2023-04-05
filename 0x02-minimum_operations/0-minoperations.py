#!/usr/bin/python3

"""
    Method to determine the quantity of minmum operations in n characters
"""


def minOperations(n):
   """
    Calculate the fewest number of operations needed to get 'n' H characters in a file
    """

    current = 1
    begin = 0
    count = 0
    while now < n:
        rem = n - current
        if (rem % current == 0):
            begin = current
            current += begin
            count += 2
        else:
            current += begin
            count += 1
    return count

# !/usr/bin/python3

#     """
#     Calculate the fewest number of operations needed to get 'n' H characters in a file
#     """
#     def minOperations(n):
#     count = 0
#     while n > 1:
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n -= 1
#         count += 1
#     return count
