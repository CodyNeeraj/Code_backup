# largest palindrome made from the product of two 3-digit numbers
def isPal(num):
    num = str(num)
    if num.lower() == num[::-1].lower():
        return True
    return False
num = 0
lis= []
for i in range(100,1000):
    for j in range(100,1000):
        lis.append(i*j)
lis = list(sorted(set(lis)))
lis = [x for x in lis if isPal(x)]
print(lis[-1])
