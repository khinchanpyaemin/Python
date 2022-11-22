import shelve
import re

itemname = []
def additem():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    a = []
    while 1:
        print("Enter done to stop")
        item = input("Enter item name(eg.milk/1litre): ")
        item = item.lower()
        if item == "done":
            break
        a.append(item)
        iteminfo =input("Enter price and quantity of the item(eg.1200 100): ")
        file[item] = iteminfo.split()
    print("{:40} {:20} {}".format('Item Name', 'Price(for each)', "Quantity"))
    for key, value in file.items():
        key = str(key).strip()
        if key in a:
            print("{:40} {:20} {}".format(key, value[0], value[1]))
    file.close()

def customerorder():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    b =[]
    bill = []
    cname =input('Enter customer name and phone number(Eg.bam(095555555): ')
    cname = cname.lower()
    while 1:
        print("Enter done to stop")
        corder= input("Enter itemname and itemquantity ordered(eg.Milk/1litre 10): ")
        corder.lower()

        if corder == "done":
            break
        s = corder.split()
        if int(s[1]) > int(file[s[0]][1]):
            print("The quantity of",s[0],"is only",file[s[0]][1],'left')
            print("Would u like to order less than or equal ",file[s[0]][1],"of the item?")
            x = input("\nEnter ur choice:(y/n): ")
            if x == "y":
                ask = input("Enter the quantity:")
                s[1] = ask
                b.append(s)
            else:
                continue
        else:
            b.append(s)
    file[cname] = b
    for v in file[cname]:
        for key,value in file.items():
            key = str(key).strip()
            if v[0] == key:
                newquantity = int(value[1]) - int(v[1])
                file[key] = [value[0],newquantity]
                x = int(value[0]) * int(v[1])
                bill.append(x)
    print("{:40} {:30} {}".format('\nName(phone number)', 'Item name', "Quantity"))
    for i in file[cname]:
        print("{:39} {:30} {}".format(cname,i[0],i[1]))
    totalamount = sum(bill)
    print("Total amount is",totalamount,"Ks")
    print("YOur order is comfirmed.Thanks")
    file.close()

def print_citemfile():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    print("{:40} {}".format('Item Name', 'Price[Ks](for each)'))
    for key,value in file.items():
        key = str(key).strip()
        if not key.endswith(')'):
            print("{:40} {}".format(key,value[0]))
def print_orderfile():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    order = []
    for key in file.keys():
        if key.endswith(')'):
            order.append(key)
    if order:
        print("{:40} {:30} {}".format('Name(phone number)', 'Ordered item name', "Ordered quantity"))
        for i in order:
            for value in file[i]:
                print("{:40} {:30} {}".format(i, value[0], value[1]))
    if not order:
        print("There is no order")
def print_itemfile():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    print("{:40} {:20} {}".format('Item Name', 'Price(for each)', "Quantity"))
    for key,value in file.items():
        key = str(key).strip()
        if key.endswith(')'):
            continue
        else:
            print("{:40} {:20} {}".format(key, value[0], value[1]))
    file.close()

def print_itemToRestore():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    zeroitem =[]
    for key,value in file.items():
        key = str(key).strip()
        if not key.endswith(')'):
            if int(value[1]) == 0:
                zeroitem.append(key)
    if zeroitem:
        print("\nThese items are no more instocked now and need to be restored")
        print('Item name')
        for i in zeroitem:
            print(i)
    if not zeroitem:
        print("\nThere is no item need to be restored")
def deleteorder():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    np = input("Enter ur name and phone number(Eg.bam(0911):")
    np = np.lower()
    for v in file[np]:
        for key,value in file.items():
            key = str(key).strip()
            if v[0] == key:
                readd = int(value[1]) + int(v[1])
                file[key] = [value[0],readd]
    file.pop(key)
    print("Successfully done")

def searchitem():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    a = input("Enter item name u want to search: ")
    a = a.lower()
    print("{:40} {}".format('Item Name', 'Price(for each)'))
    for key in file.keys():
        if not key.endswith(')'):
            itemname.append(key)
    for search in itemname:
        if re.search(a,search):
            for key, value in file.items():
                if search == key:
                    print("{:40} {}".format(key, value[0]))
def stuffMENU():
    x ='Instruction'
    print(x.center(77,'*'))
    print("{:2} {}".format("NO.","Function"))
    print('1.  To add item name,price and quantity store\n2.  To check customer order\n3.  To check item quantity\n4.  To check item that need to be restored\n5.  To update item quantity\n6.  To update item price\n7.  to delete item')

def customerMENU():
    x ='Instruction'
    print(x.center(77,'*'))
    print("{:3} {}".format("NO.", "Function"))
    print('1.  To order\n2.  To delete order\n3.  To search price of item')

def updateitemquantity():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    changeitemq =[]
    while 1:
        u = input("\nEnter item name u want to update the quantity: ")
        u = u.lower()
        if u == "done":
            break
        changeitemq.append(u)
        newq = input('Enter new quantity: ')
        file[u] = [file[u][0],newq]
    print("{:40} {:20} {}".format('\nItem Name', 'Price(for each)', "Quantity"))
    for i in changeitemq:
        print("{:39} {:20} {}".format(i, file[i][0], file[i][1]))
def updateitemprice():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    changeditem =[]
    while 1:
        u = input("Enter item name u want to update the price(enter done to stop): ")
        u = u.lower()
        if u == "done":
            break
        changeditem.append(u)
        newprice = input("Enter new price: ")
        file[u] = [newprice,file[u][1]]
    print("{:40} {:20} {}".format('\nItem Name', 'Price(for each)', "Quantity"))
    for i in changeditem:
        print("{:39} {:20} {}".format(i, file[i][0], file[i][1]))
def deleteitem():
    try:
        file = shelve.open('storagedata2')
    except FileNotFoundError:
        print("File cant be found")
    u = input("Enter item name u want to delete:")
    u = u.lower()
    for key,value in file.items():
        key = str(key).strip()
        if key == u:
            del file[key]
            print("Successfully done")
title="WELCOME TO MILKY DAIRY COMPANY"
print(title.center(90))
while 1:
    x = input('Enter your gmail account("Enter exit to stop): ')
    reg_exp = r"\w+@gmail.com"
    if not re.match(reg_exp,x):
        print("Enter the correct gmail form again")
        continue
    if x == 'exit':
        break
    if x == "TGdairycompany@gmail.com":
        while 1:
            stuffMENU()
            j =int(input("Enter function number: "))
            if j == 1:
                additem()
            if j == 2:
                print_orderfile()
            if j == 3:
                print_itemfile()
            if j == 4:
                print_itemToRestore()
            if j == 5:
                print_itemfile()
                updateitemquantity()
            if j == 6:
                print_itemfile()
                updateitemprice()
            if j == 7:
                deleteitem()
            h = input("\nContinue(y/n): ")
            if h == "y":
                continue
            else:
                break
    else:
        while 1:
            customerMENU()
            j = int(input("Enter function number: "))
            if j == 1:
                print_citemfile()
                customerorder()
            if j == 2:
                deleteorder()
            if j == 3:
                searchitem()
            h = input("\nContinue(y/n): ")
            if h == "y":
                continue
            else:
                break
