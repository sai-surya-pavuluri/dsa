"""
This module demonstrates classic recursive problems with optional memoization.
Memoization stores already-computed results to avoid redundant computation,
especially useful for overlapping subproblems.
"""

class Recursion:
    cache = {}

    @classmethod
    def clear_cache(cls):
        cls.cache.clear()

    # Fibonacci Series
    @classmethod
    def fibonacci(cls, n):
        if n in cls.cache:
            return cls.cache[n]
        if n == 0:
            cls.cache[0] = 0
        elif n == 1:
            cls.cache[1] = 1
        else:
            cls.cache[n] = cls.fibonacci(n - 1) + cls.fibonacci(n - 2)
        return cls.cache[n]
    
    # Factorial of a number
    @classmethod
    def factorial(cls, n):
        if n in cls.cache:
            return cls.cache[n]
        if n == 0:
            cls.cache[0] = 1
        elif n == 1:
            cls.cache[1] = 1
        else:
            cls.cache[n] = n * cls.factorial(n - 1)
        return cls.cache[n]



            