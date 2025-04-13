# Check if all numbers in a value from list is even or odd
import random as ra
lis = [str(x) for x in list(ra.choice(list(range(100,999))) for i in range(7))]
print(lis)
even_list =[]
odd_list =[]
for i in lis:
    trueLis =[]
    falselis =[]
    flag =False
        for j in i:
        if int(j)%2==0:
            flag =True
            trueLis.append("true")
        elif int(j)%2!=0:
            falselis.append("false")
            flag =False
                if flag == True and len(trueLis) == len(str(i)):
        even_list.append(i)
    elif flag == False and len(falselis) == len(str(i)):
        odd_list.append(i)
        print("Count of even digited numbers = ",len(even_list))
print("Count of odd digited numbers = ",len(odd_list))
