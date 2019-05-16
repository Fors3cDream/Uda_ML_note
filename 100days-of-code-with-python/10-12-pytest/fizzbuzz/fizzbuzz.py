"""
Create by Killer at 2019-05-16 09:25
"""

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'Fizz Buzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return n