def userinput():
    number = int(input("Enter a number to get its table: "))
    return number

def createtable():
    number =  userinput()
    for n in range(1,11):
        print(f"{number * n}")
     
     
createtable()