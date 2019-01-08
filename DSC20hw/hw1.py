"""
HW1 DSC20 Fall 2018
Name of Student:
PID of Student:
"""

def missing_number(lst):
    """ Given a list that contains distinct integers 0 through n 
    in any order, return the number that is missing from the list

    >>> lst = [1, 0, 3, 4]
    >>> missing_number(lst)
    2
    >>> lst = [0, 1, 4, 2]
    >>> missing_number(lst)
    3
    >>> lst = [2, 1, 5, 4, 3]
    >>> missing_number(lst)
    0
    """
    
    # YOUR CODE IS HERE #
    return int(len(lst) * (len(lst) + 1) / 2 - sum(lst))

def prime_list_reversed(x, y):
    """
    Input: the number x and y
    Output: all prime numbers within [x,y] in reverse order

    >>> prime_list_reversed(3, 10)
    [7, 5, 3]
    >>> prime_list_reversed(3, 3)
    [3]
    """
    assert isinstance(x, int)  # "first argument must be an integer"
    assert isinstance(y, int)  # "second argument must be an integer"
    assert x > 0  # "first argument must be positive"
    assert y >= x  # "second argument must be >= the first one"

    # YOUR CODE IS HERE #
    primes = [1] * y
    for i in range(2, int(y ** 0.5) + 1):
        for j in range(i + i, y + 1, i):
            primes[j - 1] = 0
    res = []
    for i in range(x, y + 1):
        if primes[i - 1] and x <= i <= y:
            res.append(i)
    return res[::-1]

def clever_average(nums):
    """
    >>> clever_average([4, 0, 100])
    4
    >>> clever_average([7, 7, 7])
    7
    >>> clever_average([-10, -4, -2, -4, -2, 0])
    -3
    """

    # YOUR CODE IS HERE #
    return int((sum(nums) - min(nums) - max(nums)) / (len(nums) - 2))

def in_or_out(outer_list, inner_list):
    """
    >>> in_or_out([-1, 0, 3, 3, 3, 10, 12], [-1, 0, 3, 12])
    True

    >>> in_or_out([3, 4, 7, 8], [2, 3, 4]) 
    False

    >>> in_or_out([2, 2, 4, 4, 6], [2, 4])
    True
    """

    # YOUR CODE IS HERE #
    return set(outer_list + inner_list) == set(outer_list)

def numbered_rows (levels = 10):
    """
    >>> numbered_rows()
    1 * 1 2 3 4 5 6 7 8 9 10 
    2 * 2 4 6 8 10 12 14 16 18 20 
    3 * 3 6 9 12 15 18 21 24 27 30 
    4 * 4 8 12 16 20 24 28 32 36 40 
    5 * 5 10 15 20 25 30 35 40 45 50 
    6 * 6 12 18 24 30 36 42 48 54 60 
    7 * 7 14 21 28 35 42 49 56 63 70 
    8 * 8 16 24 32 40 48 56 64 72 80 
    9 * 9 18 27 36 45 54 63 72 81 90 
    10 * 10 20 30 40 50 60 70 80 90 100 

    >>> numbered_rows(4)
    1 * 1 2 3 4 
    2 * 2 4 6 8 
    3 * 3 6 9 12 
    4 * 4 8 12 16 
    """
    
    # YOUR CODE IS HERE #
    for i in range(levels):
        final_str = str(i + 1) + ' * '
        for j in range(levels):
            final_str += str((i + 1) * (j + 1)) + ' '
        print(final_str)