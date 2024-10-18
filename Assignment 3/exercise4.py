
list1 = [1,34,56,78,89]

val = int(input("Enter a number: "))

for i in range(len(list1)):
    if val < list1[i]:
        list1.insert(i,val)
        print(list1)
        break       
else:
    list1.append(val)
    print(list1)


