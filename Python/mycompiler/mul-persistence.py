# persistence and getting once occuring word from a string
stri = " this is to inform all the students this is  kela to inform all the students  this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students this is to inform all the students"
myDict  = {}
for i in stri.split():
    myDict[i] = stri.count(i)
print(myDict)

for key,val in myDict.items():
    if val == 1:
        print("the only single occurence word is: ",key)

def persistence(n):
    multiplicative_persistence = 0
    while int(n) > 9:
        multiplicative_persistence += 1
        n_as_string = str(n)
        total = 1
        for i in n_as_string:
            total = total * int(i)
            n = total
    return multiplicative_persistence
print(persistence(input()))
def mul(list):
    digitArray = [int (x) for x in list]
    mul = 1
    count = 0
    while mul > 9:
        for i in digitArray:
            mul*=i
        count+=1
    return mul,count
print(myDict.keys())
print(myDict.values())
print(mul(list(myDict.values())))
print(sorted(set(stri.split())))
