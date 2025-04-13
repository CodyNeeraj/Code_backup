def perfectSqaure(lis):
    new = []
    for i in range(0,len(lis)):
        isperfect = False
        sqr = math.sqrt(lis[i])
        val = int(lis[i]//sqr)
        if lis[i] == int(sqr)*int(sqr):
            isperfect = True
            new.append(lis[i])
