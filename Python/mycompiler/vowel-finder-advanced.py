# vowel string kicker
import random as ra
from string import ascii_letters as alphas
def Novowel(strr):
    vowels = list("aeiou")
    gotVowel = False
    for char in vowels:
        if char in strr.lower():
            return True
    return False
    letters = list(alphas)
customlist = []
for i in range(10):
    temp = "".join(letters[ra.randint(1,25):ra.randrange(25)])
    if len(temp.strip())!=0:
        customlist.append(temp)
print(customlist)
lis = ["ksdgyt","neejk","dpljui"]
list_no_vwel = []
for index,item in enumerate(customlist):
    if not Novowel(item):
        list_no_vwel.append(item)
    else:
        print("string",item,"contains vowel")
print("list dont containg vowels : ",list_no_vwel)
