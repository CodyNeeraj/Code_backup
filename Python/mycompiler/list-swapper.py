# ListSwapper
list = [1,2,3,4,5,6,7,82,3,4,5,6,7,82,3,4,5]
# [1, 2, 5, 6, 3, 5, 51, 2, 5, 6, 3, 5, 51, 2, 5, 6, 3, 8, 55, 6]
# [3, 5, 51, 2, 5, 6, 3, 8, 55, 6, 1, 2, 5, 6, 3, 5, 51, 2, 5]
def swapper(list):
    newList = []
    mid =-1
    if len(list) % 2 == 0:
        print("even sized list encountered")
        mid =int((0 + len(list)-1) / 2)
        print("the mid ndex is ",mid,list[mid])
        for i in list[mid+1:]:
            newList.append(i)
        for i in list[0:mid+1]:
            newList.append(i)
    else:
        print("odd sized list is encountered")
        mid =int((0 + len(list)-1) / 2)
        print("the mid is ",mid,list[mid])
        for i in list[mid+1:]:
            newList.append(i)
        newList.append(list[mid])
        for i in list[0:mid]:
            newList.append(i)
    return newList
print(list,"\n",swapper(list))
if __name__ == "__main__":
    pass
