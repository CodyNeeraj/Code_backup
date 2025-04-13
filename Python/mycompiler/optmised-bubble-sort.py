# optimised bubble sort, Max product subarray
import random,string,time,math,functools
def bubbleSort(lis):
    length = len(lis)
    cntr = 0
    swapped = False
    for i in range(length):
        for j in range(0,length-i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1] =lis[j+1],lis[j]
                swapped =True
                cntr+=1
        if not swapped:
            break
    # print(lis)
    print(cntr)
    print(length)
if __name__ == "__main__":
    start = time.time()
    lis = list(random.choice(string.digits) for x in range(10000))
    bubbleSort(lis)
    stop = time.time()
    print("Elapsed time =  {:.6f}".format(stop-start))
