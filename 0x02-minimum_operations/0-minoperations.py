# #!/usr/bin/python3

# """
#     Method that determines the number of minmum operations given n characters
# """


# def minOperations(n):
#     '''
#     calculates the fewest number of operations
#         needed to give a result of exactly n H characters in a file
#         args: n: Number of characters to be displayed
#         return:
#                number of min operations
#     '''

#     now = 1
#     start = 0
#     counter = 0
#     while now < n:
#         rem = n - now
#         if (rem % now == 0):
#             start = now
#             now += start
#             counter += 2
#         else:
#             now += start
#             counter += 1
#     return counter

!/usr/bin/python3
def minOperations(n):
    """
    Calculate the fewest number of operations needed to get 'n' H characters in a file
    """
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        count += 1
    return count
