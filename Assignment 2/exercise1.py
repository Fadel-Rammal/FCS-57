

print("The values must be in the range of this list")
print("[54,76,2,4,98,100]")

list1 = [54,76,2,4,98,100]

int1 = int(input("Enter int1: "))
int2 = int(input("Enter int2: "))

i=0

if int1 > int2:
    print("int1 must be less than int2")
else:
    while i < len(list1):
        if list1[i]>int1 and list1[i]<int2:
            print(list1[i])
        i+=1
        

print("Done")
        









