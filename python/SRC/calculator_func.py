
def menu():
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 0 for Exit")

menu()

def numbers_input():
        while True:
            first_number = input("Enter First Number: ")
            if first_number.isdigit():
                first_number = int(first_number)
                while True:
                    second_number = input("Enter Second Number: ")
                    if second_number.isdigit():
                        second_number = int(second_number)
                        break
                break 
        return first_number,second_number    

def addition():
    first_num,second_num = numbers_input()
    return first_num + second_num

def subtraction():
    first_num,second_num = numbers_input()
    return first_num - second_num

def multiplication():
    first_num,second_num = numbers_input()
    return first_num * second_num

def division():
    first_num,second_num = numbers_input()
    # if second_num !=0:
    return first_num / second_num
    # else:

       
while True:
    menuinput = input("Enter Task no: ")
    if menuinput.isdigit():
        menuinput = int(menuinput)
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
    else:
        print("Enter valid Task Number")
