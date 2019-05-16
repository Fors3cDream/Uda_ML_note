"""
Create by Killer at 2019-05-16 09:14
"""

numlist = [1, 2, 3, 4, 5]

print(numlist)

numlist.reverse()
print("Reverse numlist: ", numlist)

mystring = "killer"

for i in list(mystring):
    print(i)


l = list(mystring)
t = tuple(mystring)

print(l)
print(t)

print(l[0] == 'b')
l[0] = 'b'
print("After update : ", l)

try:
    t[0] = 'm'
except Exception as e:
    print(str(e))

l.pop(0)

print("After pop : ", l)

l.insert(0, "M")
print("After insert : ", l)

del l[0]
print("After del :", l)

# Dicts
pybites = {'julian': 30, 'bob': 33, 'mike': 33}
print(pybites)

print("Keys:",pybites.keys())

print("Values:", pybites.values())

for keys in pybites.keys():
    print(keys)

for keys, values in pybites.items():
    print(f'{keys} is {values} years of age!')