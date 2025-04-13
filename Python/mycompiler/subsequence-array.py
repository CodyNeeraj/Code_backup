# subsequences of string /array
def Subsequences(arr):
    output = [[]]
    for i in arr:
        output+=[lst +[i] for lst in output]
        print(output)
    return output

if __name__ == "__main__":
    x =Subsequences("abc")
    print()
    for df in x:
        print(df)
    print(len(x))
