# occuring permutation in a string
import random
mystr = "".join(random.choice(list("aabbccddda"))for i in range(10))

print("Original string is: ",mystr)

set_window_size = 3
anagram_to_find ="bcd"
temp = None


for i in range(len(mystr)):
    temp = mystr[i:i+3]
    if "".join(sorted(temp)) == anagram_to_find:
        print("Match found at ",temp,mystr.index(temp))
    else:
        print("no match is found")
