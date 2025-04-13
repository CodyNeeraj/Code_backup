# lcm of a series
import functools
from math import gcd
lis = list(range(1,21))
print(functools.reduce(lambda a,b: a*b//gcd(a,b),lis))

#another approach
# a = [100, 200, 150]   #will work for an int array of any length
# lcm = 1
# for i in lis:
#     lcm = lcm*i//gcd(lcm, i)
# print(lcm)
