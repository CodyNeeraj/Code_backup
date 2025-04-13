import random,string

def addingUp(arr):
        if len(arr)== 1:
        return arr [0]
            if len(arr) == 0:
        return 0
            return arr[0] + addingUp(arr[1:])

max_len  = int(input())
mylis =[int(x) for x in list(random.choice(string.digits) for i in range(max_len))]
print(mylis)

# custom test case for verification
# mylis =[0,1,2,3,5]

ans = addingUp(mylis)
print(ans)
print(ans == sum(mylis))
