# Kth rotation
lis =  tuple(range(0,26))
print(lis)
'''
   our task is to make the above list cyclically rotatable
   upto the kth element i.e as told in the user input
   for ex: if the input is of 3 then the last 3 elements of
   the above list's are repositioned until they all get onto
   front of list and each other leftover elements are slided
   to right !!!
'''
rt = int(input())
if rt>len(lis)-1:
    print("You can't enter a shift value of more than the size of array")
elif rt <= 0:
    print("chutiye  zero krega mc")
else:
    kth = len(lis)-rt
    print(kth,"the element is ",lis[kth])
    new_list = list()
    for i in lis[kth:]:
        new_list.append(i)
        print(new_list)
    for i in lis[0:kth]:
        new_list.append(i)
        print(new_list)
    print(new_list)
