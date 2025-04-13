# Sort 012
import random as ra

def func(lis):
    cntr0,cntr1,cntr2 =0,0,0
    for i in lis:
        if i == 0:
            cntr0+=1
        elif i==1:
            cntr1+=1
        elif i ==2:
            cntr2+=1
    return [cntr0,cntr1,cntr2]
         lis =list(ra.choice([0,1,2]) for i in range(100))
print(lis.count(1))
print(lis)
x = func(lis)
lis.clear()
while x[0]!=0:
    lis.append(0)
    x[0]-=1
while x[1]!=0:
    lis.append(1)
    x[1]-=1
while x[2]!=0:
    lis.append(2)
    x[2]-=1
print(lis)
print(lis.count(1))
