# Matrix manipulations python
#getting input for a matrix of specified rows and columns
n = int(input())
mat=[]
for i in range(n):
    data =[] # emptying list in mandatory
    for j in range(n):
        data.append(int(input()))
    mat.append(data)
print(mat)

# see the below index translation for reference
# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

#diagonal sum of above matrix
val =0
sec =0
for i in range(n):
    for j in range(n):
        if i == j:
            val+=mat[i][j]
        if i+j == n-1:
            sec+=mat[i][j]
            print("digonal sum is for left = {} and right = {} ".format(val,sec))
print("diff is ",val-sec)


#also the O(n) solution:
# for i in range(0, n):
#     principal += mat[i][i]
#     secondary += mat[i][n - i - 1]
