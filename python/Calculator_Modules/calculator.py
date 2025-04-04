import addnum
import subnum
import multiplynum
import dividenum

def menu():
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 0 for Exit")

menu()

while True:
    menuinput = input("Enter Task no: ")
    if menuinput.isdigit():
        menuinput = int(menuinput)
        if menuinput == 1:
            print("Addition is ",addnum.addition())
        elif menuinput == 2:
            print("Subtraction is",subnum.subtraction())
        elif menuinput == 3:
            print("Multiplication is",multiplynum.multiply())
        elif menuinput == 4:
            print("Division is",dividenum.divide())
        elif menuinput == 0:
            break
        else:
            print("Choose valid option ")
    else:
        print("Enter valid Task Number")