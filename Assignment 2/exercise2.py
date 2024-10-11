
Names=["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

letter = input("Enter a letter: ")

i = 0

if len(letter) != 1:
    print("enter one letter")

else:
    while i < len(Names):
        if letter in Names[i]:
            print(Names[i])
        i+=1
print("Done")









