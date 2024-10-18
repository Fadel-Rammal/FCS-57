
dict = {'juice':5, 'potato':10, 'chocolate':7}
dictdet = {}

def receiptdet():

    barc = input("Enter item barcode: ")
    quan = int(input("Enter the quantity client purchased: "))

    dictdet[barc]=quan
   

    newreceipt()

def newreceipt():
    newr = input("Do you want to start a new receipt: ")
    if newr.lower() == "yes": 
        receiptdet()
    elif newr.lower() == "no":
        total = 0
        for key, value in dictdet.items():
            price = dict[key]
            item_total = price * value
            total += item_total
            print(f"{key} \n Quantity:{value} Total Item Price= {item_total}")
            print("Total Price is: ", total)
            
        dictdet.clear() 
        exit()

newreceipt()

