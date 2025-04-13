# Program to find if a number is power of two
import math

'''
for calculating the log 2 of any number the formula is
                 log 2 = log10(num)
                     ----------
                      log10(2)
    #code by Neeraj
    where log10 is the natural log with common base 10 as usually found in calculaters!!
'''

def Log2(x):
 if x == 0:
  return False;

 return (math.log10(x) / math.log10(2));

def isPowerOfTwo(n):
    #computing both the upper and lower limit of a number !
 return (math.ceil(Log2(n)) == math.floor(Log2(n)));

if __name__ == "__main__":
    lis = [x for x in range(50000) if isPowerOfTwo(x)]
    print(lis)
