# fibonacci timer
a,b = 0,1

# lis= []
# for i in range(1000):
#     a=a+b
#     b=a
#     c=b
#     lis.append(c)
# print(len(lis))
lis= []
for i in range(400000):
    c=a+b
    a=b
    b=c
    lis.append(c)

new =[x for x in lis if x%2 ==0]
print(new)

# new = [x for x in new if x%2 ==0]
print(new)
print(sum(new))

import time
start = time.time()
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        #return quotient and remainder => num/den = quotient(0) and remainder (num) only for this case where den = 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    stop = time.time()
    print('Fire in the hole!!')
    print("Script exceution took {:.2f} seconds".format(stop-start))
countdown(int(5))
