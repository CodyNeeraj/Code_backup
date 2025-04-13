# armstronger
a = 2063
lis =[]
def armstring_finder(num):
    ans=0
    mylis = list(int(x) for x in str(num))
    for i in mylis:
        ans+=i**len(mylis)
    return ans == num
    new = [x for x in range(0,100000) if armstring_finder(x)]
# print(new[::-1])
for i in new[::-1]:
    print(i)
print(new)
# for i in range(0,1000):
#     print("is {} and armstrong number : {}".format(i,armstring_finder(i)))
# temp =a
# while temp > 0:
#     digit = temp%10
#     temp //=10
#     lis.append(digit)
# new =[lis[x] for x in range(len(lis)-1,0,-1)]
# print(new)
