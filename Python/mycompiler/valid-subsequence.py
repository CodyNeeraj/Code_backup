// Valid Subsequence
import random
def isValidSubsequence(array,seq):
    arrIdx = 0
    seqidx = 0
        while arrIdx<len(array) and seqidx < len(seq):
        if array[arrIdx] == seq[seqidx]:
            seqidx+=1
        arrIdx+=1
    return seqidx == len(seq)

data = list(range(0,10))
random.shuffle(data)
print(data)
print(isValidSubsequence(data,[2,4]))
