# Numeric to Word converter
arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
  def number_2_word(n):
     # If all the digits are encountered return blank string
    if n==0:
        return ""
         elif n!=0:
        #here computing the first digit in given argument andn using basic
        #logic of getting a same number when modulus is computed by 10
        small_ans = arr[n%10]
         # keep computing for the previous digits and add the spelling for the last digit
        # Basically using recursion to store the previous results
        ans = number_2_word(int(n//10)) +small_ans + " "
         return ans
  n = int(input())
print("Number Entered was : ", n)
print("Converted to word it becomes: ",end="")
print(number_2_word(n))
