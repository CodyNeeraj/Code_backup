# subarrays and repeating pattern
su = "jkajfa"
stri =list(su)
print(stri)
l = len(stri)
print("the total combinations are: ",int((l*(l+1))/2-1))
for i in range(len(stri)):
    for j in range(i,len(stri)):
        print(stri[i:j+1])
        
# Above solution basically comes as
# ['j', 'k', 'a', 'j', 'f', 'a']
# the total combinations are:  20

# 1 ['j']
# 2 ['j', 'k']
# 3 ['j', 'k', 'a']
# 4 ['j', 'k', 'a', 'j']
# 5 ['j', 'k', 'a', 'j', 'f']
# 6 ['j', 'k', 'a', 'j', 'f', 'a']
# 7 ['k']
# 8 ['k', 'a']
# 9 ['k', 'a', 'j']
# 10 ['k', 'a', 'j', 'f']
# 11 ['k', 'a', 'j', 'f', 'a']
# 12 ['a']
# 13 ['a', 'j']
# 14 ['a', 'j', 'f']
# 15 ['a', 'j', 'f', 'a']
# 16 ['j']
# 17 ['j', 'f']
# 18 ['j', 'f', 'a']
# 19 ['f']
# 20 ['f', 'a']
# 21 ['a']

test_str = "thisismethisismethisismethisismethisismethisismethisismethisismethisismethisisme"
l = len(test_str)
print("the total combinations are: ",int((l*(l+1))/2-1))
res = None
temp = (test_str + test_str).find(test_str, 1, -1)
print(temp)
if temp != -1:
    res = test_str[:temp]
  print("The root substring of string : " + res)

