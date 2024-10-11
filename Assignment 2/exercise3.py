
numbers = [-12, 4, 12, 25, 67]

while True:
    n = int(input("Enter a number: "))
    

    if n == -99:
        break

    for i in range(len(numbers)):
        if n < numbers[i]:
            numbers.insert(i,n)
            print(numbers)
            break
    else: 
        numbers.append(n)
        print(numbers)
        

print(numbers)
