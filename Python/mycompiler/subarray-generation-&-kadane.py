# subarray generator and sum checker /kadane algo
import time
str = "13465465656565556555"
str_array =[int (x) for x in str]
my_dict = dict()
start = time.time()
for i in range(len(str_array)):
    for j in range(i,len(str_array)):
        total = sum(str_array[i:j+1])
        my_dict[total] = str_array[i:j+1]
maxm_key =[x for x in sorted(my_dict.keys(),key=lambda x:my_dict[x])]
stop = time.time()
print("{:.2f}".format(stop-start))
print(maxm_key)

def kadane():
    max_till_now =0
    max_ending =0
    for i in range(len(str_array)):
            max_ending = max_ending + str_array[i]
            if (max_ending < 0):
                max_ending =0
            elif max_ending > max_till_now:
                max_till_now =max_ending
    print(my_dict[max_till_now])
    kadane()
