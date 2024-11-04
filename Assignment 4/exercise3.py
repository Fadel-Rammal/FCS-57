
s1 = []
n = input("Enter a word: ")

for i in n:
    if i != '*':
        s1.append(i)
    elif i == '*':
        s1.pop()

print(''.join(s1))

