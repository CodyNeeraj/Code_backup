# Dynamic Programming starting in Python using optimal sub-solution and overlapping subproblem
# Dynamic programming with top to bottom approach using memoisation
# simple recursive solution with a dp_array

def fib(n,dp_array):
    if (n<=1):
        return n
            if dp_array[n] !=-1:
        return dp_array[n]
            dp_array[n]= fib(n-1,dp_array)+fib(n-2,dp_array)
    return dp_array[n]

val = int(input()) # value to be find in the dp_array of memoisation
dp_array =[-1]*(val+1) # initialistion of the dp_array

print(fib(val,dp_array)) #computing the result and printing the output

# Tabulation method (with memoisation)
# simple backvieiwing and computing the next adjacent sum of the series !

def fib(val,dp):
    for i in range(2,val+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[i]
    val = int(input())
dp_array = [-1]*(val+1)
dp_array[0]=0
dp_array[1]=1
print(fib(val,dp_array))
