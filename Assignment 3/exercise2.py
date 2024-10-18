
def combination(n, c,str1):

    if n==0:
        print(str1)
        return

    for i in range(len(characters)):
        cc = c[i]
        combination(n-1,c,str1+cc)

n = int(input("Enter needed length: "))
characters = ["a", "b", "c"]
combination(n, characters,"")

