# random password spammer
import random as ra
import string
def swapper():
        chr = ''.join(ra.choice(string.ascii_lowercase + string.ascii_uppercase + "^$@*&@^$*&)%"))
    print(chr,end="\r")
# print(str(chr))
for i in range(50000):
    swapper

