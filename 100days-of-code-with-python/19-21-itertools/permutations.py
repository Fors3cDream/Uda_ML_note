"""
Create by Killer at 2019-05-16 16:04
"""

from itertools import permutations, combinations

friends = 'mike bob julian'.split()


# note that we get a generator to using list to consume it
print(list(combinations(friends, 2)))


# what if order matters?
print(list(permutations(friends, 2)))