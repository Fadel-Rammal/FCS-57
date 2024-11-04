
s1 = []
s2 = []
n = input("Enter a word: ")

for i in n:
    print(i)
    s1.append(i)
print(s1)

for i in n[::-1]:
    print(i)
    s2.append(i)
print(s2)

if s1 == s2:
    print("the word is palindrome")
else:
    print("the word is not palindrome")
