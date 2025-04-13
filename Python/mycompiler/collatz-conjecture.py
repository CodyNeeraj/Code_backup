# Collatz Conjecture
def collatzConjec(num):
    val = num
    lis =[]
    lis.append(val)
    while(val>1):
        if val %2==0: #its the even boi
            val//=2
            lis.append(val)
        elif val %2!=0:
            val = (3*val)+1
            lis.append(val)
    chain_length = len(lis)
    lis.clear()
    return (chain_length,num)


if __name__ == "__main__":
    mylis= []
    for i in range(1000000):
        mylis.append(collatzConjec(i))
    print(sorted(mylis,key=lambda n:n[0]))
