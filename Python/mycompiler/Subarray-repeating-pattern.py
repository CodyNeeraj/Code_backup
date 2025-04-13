# subarrays and repeating pattern
su = "jkajfa"
stri =list(su)
print(stri)
l = len(stri)
print("the total combinations are: ",int((l*(l+1))/2-1))
for i in range(len(stri)):
    for j in range(i,len(stri)):
        print(stri[i:j+1])
test_str = "thisismethisismethisismethisismethisismethisismethisismethisismethisismethisisme"
l = len(test_str)
print("the total combinations are: ",int((l*(l+1))/2-1))
res = None
temp = (test_str + test_str).find(test_str, 1, -1)
print(temp)
if temp != -1:
    res = test_str[:temp]
  print("The root substring of string : " + res)

