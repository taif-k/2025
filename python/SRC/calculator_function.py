
def menu():
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 0 for Exit")

menu()

def addition():
    first_number = int(input("Enter First Number: "))
    second_number = int(input("Enter Second Number: "))
    return first_number + second_number

def subtraction():
    first_number = int(input("Enter First Number: "))
    second_number = int(input("Enter Second Number: "))
    return first_number - second_number

def multiplication():
    first_number = int(input("Enter First Number: "))
    second_number = int(input("Enter Second Number: "))
    return first_number * second_number

def division():
    first_number = int(input("Enter First Number: "))
    second_number = int(input("Enter Second Number: ")) 
    return first_number/second_number
       

while True:
    menuinput = int(input("Enter Task no: ")) 
    if menuinput == 1:
        print("Addition is ",addition())
    elif menuinput == 2:
        print("Subtraction is ",subtraction())
    elif menuinput == 3:
        print("Multiplication is ",multiplication())
    elif menuinput == 4:
        print("Division is ",division())
    elif menuinput == 0:
        break
    else:
        print("Choose valid option ")
