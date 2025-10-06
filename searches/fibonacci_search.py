"""
This is pure Python implementation of fibonacci search.

Resources used:
https://en.wikipedia.org/wiki/Fibonacci_search_technique

For doctests run following command:
python3 -m doctest -v fibonacci_search.py

For manual testing run:
python3 fibonacci_search.py
"""

from functools import lru_cache


@lru_cache
def fibonacci(k: int) -> int:
    """Finds fibonacci number in index k.

    Parameters
    ----------
    k :
        Index of fibonacci.

    Returns
    -------
    int
        Fibonacci number in position k.

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> fibonacci(8)
    21
    >>> fibonacci(10)
    55
    >>> fibonacci(15)
    610
    >>> fibonacci(20)
    6765
    >>> fibonacci('a')
    Traceback (most recent call last):
    TypeError: k must be an integer.
    >>> fibonacci(-5)
    Traceback (most recent call last):
    ValueError: k integer must be greater or equal to zero.
    >>> fibonacci(-1)
    Traceback (most recent call last):
    ValueError: k integer must be greater or equal to zero.
    >>> fibonacci(None)
    Traceback (most recent call last):
    TypeError: k must be an integer.
    >>> fibonacci(3.14)
    Traceback (most recent call last):
    TypeError: k must be an integer.
    >>> fibonacci("5")
    Traceback (most recent call last):
    TypeError: k must be an integer.
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    if k < 0:
        raise ValueError("k integer must be greater or equal to zero.")
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)


def fibonacci_search(arr: list, val: int) -> int:
    """A pure Python implementation of a fibonacci search algorithm.

    Parameters
    ----------
    arr
        List of sorted elements.
    val
        Element to search in list.

    Returns
    -------
    int
        The index of the element in the array.
        -1 if the element is not found.

    # Basic functionality tests
    >>> fibonacci_search([4, 5, 6, 7], 4)
    0
    >>> fibonacci_search([4, 5, 6, 7], 5)
    1
    >>> fibonacci_search([4, 5, 6, 7], 6)
    2
    >>> fibonacci_search([4, 5, 6, 7], 7)
    3
    >>> fibonacci_search([4, 5, 6, 7], -10)
    -1
    >>> fibonacci_search([4, 5, 6, 7], 10)
    -1

    # Edge case: empty list
    >>> fibonacci_search([], 1)
    -1
    >>> fibonacci_search([], 0)
    -1
    >>> fibonacci_search([], 9)
    -1

    # Edge case: single element
    >>> fibonacci_search([5], 5)
    0
    >>> fibonacci_search([5], 3)
    -1
    >>> fibonacci_search([5], 7)
    -1
    >>> fibonacci_search([0], 0)
    0
    >>> fibonacci_search([-1], -1)
    0

    # Two elements
    >>> fibonacci_search([-18, 2], -18)
    0
    >>> fibonacci_search([-18, 2], 2)
    1
    >>> fibonacci_search([-18, 2], 0)
    -1
    >>> fibonacci_search([1, 2], 1)
    0
    >>> fibonacci_search([1, 2], 2)
    1
    >>> fibonacci_search([1, 2], 0)
    -1
    >>> fibonacci_search([1, 2], 3)
    -1

    # Three elements
    >>> fibonacci_search([1, 2, 3], 1)
    0
    >>> fibonacci_search([1, 2, 3], 2)
    1
    >>> fibonacci_search([1, 2, 3], 3)
    2
    >>> fibonacci_search([1, 2, 3], 0)
    -1
    >>> fibonacci_search([1, 2, 3], 4)
    -1

    # String elements
    >>> fibonacci_search(['a', 'c', 'd'], 'a')
    0
    >>> fibonacci_search(['a', 'c', 'd'], 'c')
    1
    >>> fibonacci_search(['a', 'c', 'd'], 'd')
    2
    >>> fibonacci_search(['a', 'c', 'd'], 'b')
    -1
    >>> fibonacci_search(['a', 'c', 'd'], 'f')
    -1
    >>> fibonacci_search(['apple', 'banana', 'cherry'], 'banana')
    1

    # Float elements
    >>> fibonacci_search([.1, .4 , 7], .1)
    0
    >>> fibonacci_search([.1, .4 , 7], .4)
    1
    >>> fibonacci_search([.1, .4 , 7], 7)
    2
    >>> fibonacci_search([0.1, 0.2, 0.3, 0.4, 0.5], 0.3)
    2
    >>> fibonacci_search([1.1, 2.2, 3.3], 2.2)
    1

    # Negative numbers
    >>> fibonacci_search([-10, -5, -1, 0, 1, 5], -10)
    0
    >>> fibonacci_search([-10, -5, -1, 0, 1, 5], -5)
    1
    >>> fibonacci_search([-10, -5, -1, 0, 1, 5], 0)
    3
    >>> fibonacci_search([-10, -5, -1, 0, 1, 5], 5)
    5
    >>> fibonacci_search([-10, -5, -1, 0, 1, 5], -15)
    -1

    # Larger lists - test different fibonacci search paths
    >>> fibonacci_search(list(range(100)), 0)
    0
    >>> fibonacci_search(list(range(100)), 1)
    1
    >>> fibonacci_search(list(range(100)), 50)
    50
    >>> fibonacci_search(list(range(100)), 63)
    63
    >>> fibonacci_search(list(range(100)), 99)
    99
    >>> fibonacci_search(list(range(100)), 100)
    -1
    >>> fibonacci_search(list(range(100)), -1)
    -1

    # Test with step ranges
    >>> fibonacci_search(list(range(-100, 100, 3)), -100)
    0
    >>> fibonacci_search(list(range(-100, 100, 3)), -97)
    1
    >>> fibonacci_search(list(range(-100, 100, 3)), 0)
    -1
    >>> fibonacci_search(list(range(-100, 100, 3)), 98)
    66
    >>> fibonacci_search(list(range(-100, 100, 5)), 0)
    20
    >>> fibonacci_search(list(range(-100, 100, 5)), 95)
    39
    >>> fibonacci_search(list(range(-100, 100, 5)), -100)
    0
    >>> fibonacci_search(list(range(-100, 100, 5)), -95)
    1

    # Test with duplicates (algorithm may not find first occurrence)
    >>> fibonacci_search([1, 2, 2, 2, 3], 2)
    3
    >>> fibonacci_search([1, 1, 1, 2, 3], 1)
    2
    >>> fibonacci_search([0, 0, 0, 0, 1], 0)
    3

    # Fibonacci sequence lengths that trigger different search paths
    >>> fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8], 1)  # 8 elements = F_6
    0
    >>> fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8], 8)
    7
    >>> fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8], 4)
    3
    >>> fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8], 9)
    -1

    # 13 elements = F_7
    >>> test_list_13 = list(range(1, 14))
    >>> fibonacci_search(test_list_13, 1)
    0
    >>> fibonacci_search(test_list_13, 13)
    12
    >>> fibonacci_search(test_list_13, 7)
    6
    >>> fibonacci_search(test_list_13, 14)
    -1

    # 21 elements = F_8
    >>> test_list_21 = list(range(1, 22))
    >>> fibonacci_search(test_list_21, 1)
    0
    >>> fibonacci_search(test_list_21, 21)
    20
    >>> fibonacci_search(test_list_21, 11)
    10
    >>> fibonacci_search(test_list_21, 22)
    -1
    """
    len_list = len(arr)
    # Find m such that F_m >= n where F_i is the i_th fibonacci number.
    i = 0
    while True:
        if fibonacci(i) >= len_list:
            fibb_k = i
            break
        i += 1
    offset = 0
    while fibb_k > 0:
        index_k = min(
            offset + fibonacci(fibb_k - 1), len_list - 1
        )  # Prevent out of range
        item_k_1 = arr[index_k]
        if item_k_1 == val:
            return index_k
        elif val < item_k_1:
            fibb_k -= 1
        elif val > item_k_1:
            offset += fibonacci(fibb_k - 1)
            fibb_k -= 2
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
