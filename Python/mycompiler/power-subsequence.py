# Power Set / Subsequence
# Reidentation required 
import math;
def printPowerSet(lis,lis_len):
   pow_set_size = (int)(math.pow(2, lis_len))
   counter = 0
   j = 0
   for counter in range(0, pow_set_size):
      for j in range(0, lis_len):
       # Check if jth bit in the counter is set, If set then print jth element from set
       #performing AND operation between counter value and left shifted 1 by j times
         if((counter & (1 << j)) > 0):
            print(lis[j], end = "")
  print("")

lis = ['a', 'b', 'c'];
printPowerSet(lis, len(lis));
