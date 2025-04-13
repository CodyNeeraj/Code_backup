#implementation of countings sort 
import random as ra

# mylis = list(map(int,list(ra.choice("0123456789") for i in range(10))))
mylis = list(ra.choice(list(range(0,15) ))for i in range(15))
print("Original List ",mylis)

newlis=[0]*len(mylis) #initialising the auxilary array of default zero values

for i in mylis:
    newlis[i]=newlis[i]+1 #incrementing the counter of specific existing indexes
print(newlis)
for i in range(len(newlis)):
    try:
        newlis[i+1]=newlis[i]+newlis[i+1] #incrementing the contiguous elements
    except Exception as e:
        pass # for AEOB Exception
      
# newlis.pop() #removing the last extra element from above operation
print(newlis)
print(newlis.pop(newlis[0])) #left shifting the whole aux array
print(newlis)
