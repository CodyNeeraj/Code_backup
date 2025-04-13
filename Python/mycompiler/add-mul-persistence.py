# additive/multiplicative persistence
def additive_persistence(num):
    steps = 0
    while num > 9:
        temp =1
        stringify = str(num)
        mylis = list(stringify)
        lisofdigits = [int(x) for x in mylis]
        for i in lisofdigits:
            temp*=i
            # num =temp
            # num = sum(lisofdigits)
        num =temp
        print(temp)
        steps+=1
    return steps

print(additive_persistence(165))
