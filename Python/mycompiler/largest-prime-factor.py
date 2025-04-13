# Biggest prime factor of a number
import math
num  = 600851475143  # big numbered value need to be finded the factor of !
sqrt  = int(math.sqrt(num))

mylis =[]
mylisnew =[]

# here we are calculating the sqrt of the number and going upto
# that limit in search of possible factors of it by dividing
# the range of sqrted numbers with the actual big number given
# into and then taking the last factor in the range and then using
# that number to further calculate the factor until end of its range.

def isPrime(value): # for checking is the number is Prime or not
    for i in range(2,value+1):
        if value % i == 0:
            return True
    return False
    for i in range(1,sqrt+1): # for calculating the factors by first sqrting the num
    if (num % i == 0):
        mylis.append(i)

calc_num = mylis[-1] # for fetching the last value in the list

for i in range(1,calc_num): # for calculating the factors of last value given above
    if (calc_num % i == 0):
        mylisnew.append(i)
        mylisnew = [x for x in mylisnew if isPrime(x)] #filtering out the prime numbers only

print("the largest prime factor of the {} is {}".format(num,mylisnew[-1]))
