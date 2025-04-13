# Gaussian Series Summation Computation
def sumofSquares(num):
    ans = ((num*(num+1))*(2*num+1))//6
    return ans

def SquareofSUMS(num):
    ans = (num*(num+1)//2)**2
    return ans
    def sumofNms(num):
    ans = num*(num+1)//2
    return ans
    def diff(x):
    sumsqrs =  sumofSquares(x)
    sqrofsum = SquareofSUMS(x)
    print(sqrofsum-sumsqrs)
    return sumsqrs - sqrofsum
            # print(sumofSquares(10))
print(diff(100))
print((sumofNms(100)**2)-sumofSquares(100))
