# Sorted Array Checker using recursion
import random
import string
def isSorted(arr,size):
        if len(arr)== 1 or len(arr) == 0:
        return True
            if arr[0]> arr[1]:
        return False
    # If array's first and second element is in order and the next
    # possible iteration of the recursion gives True until the end of the
    # array so we can use the above given scenario with full ease !
    # in this particular line of arr slicing using : symbol, the given array
    # gets sliced into its leftovre counterpart than the previous given array and
    # keep on continuing so until the array gets exhausted.
        return arr[0] <= arr[1] and isSorted(arr[1:],len(arr))

mylis =[int(x) for x in list(random.choice(string.digits) for i in range(4))]
print(mylis)
# custom test case for verification
# mylis =[0,1,2,3,5]
res =isSorted(mylis,len(mylis))

if res:
    print("the given array is sorted !!")
else:
    print("the given array is not sorted !!")
