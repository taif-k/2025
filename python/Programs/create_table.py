def userinput():
    number = int(input("Enter a number to get its table: "))
    return number

def createtable(num):
    for n in range(1,11):
        print(f"{num * n}")
     
     
createtable(userinput())


# or 

def userinput():
    number = int(input("Enter a number to get its table: "))
    return number

def createtable():
    num  = userinput()
    for n in range(1,11):
        print(f"{num * n}")
     
     
createtable()