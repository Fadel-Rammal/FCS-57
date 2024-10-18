

def binarysearch(list1,key,start,end):
    
    if start<=end:
        mid=(start+end)//2
        if list1[mid]==key:
            return True
        elif list1[mid]<key:
           return binarysearch(list1,key,mid+1,end)
        else:
           return binarysearch(list1,key,start,mid-1)
    else:
        return False

list1=[12,14,15,44,54,64,78]
print(binarysearch(list1,12,0,len(list1)-1))
print(binarysearch(list1,78,0,len(list1)-1))
print(binarysearch(list1,15,0,len(list1)-1))
print(binarysearch(list1,-1,0,len(list1)-1))
print(binarysearch(list1,100,0,len(list1)-1))






