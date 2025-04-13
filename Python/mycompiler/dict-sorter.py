# dictionary sorter
import random
ky = list(range(0,5))
random.shuffle(ky)
mydict = dict()
for valu in ky:
    mydict[valu] = random.randint(5,10)
print(mydict)
def jk(x):
    return x[1]
    val =[]
# mydict = {k:v for k,v in sorted(mydict.items(),key=jk)}
        #   k:v for k,v in sorted(dt.items(), key=lambda item: item[1])}
for k,v in sorted(mydict.items(),key=jk):
    mydict[k]=v
print(mydict)
print(val)
