# Minimum jumps required for getting to a particular stair Dynamic programming
#this method is based on simple recursion basis
MOD = 10000000007 # a given in the question

def solve(nStairs,i):
    if(i == nStairs):
    # we're at the same stairs where we want to go actually
        return 1
            if(i > nStairs):
        return 0


    return (solve(nStairs,i+1)+ solve(nStairs,i+2)) % MOD
    #generating the base mechanism of recursion tree of
    # same repeating outputs !

def countDistinctWayToClimbStair(nStairs):
    ans = solve(nStairs,0)
    return ans
    print(countDistinctWayToClimbStair(20))
