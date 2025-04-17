import error_log
import datetime
import error_source

def menu():
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 0 for Exit")

def numbers_input():
        try:
            first_number = int(input("Enter first number"))
            second_number = int(input("Enter second number"))
            return first_number,second_number
        except Exception as e:
            print("Numbers should be in digits only")    
            date = datetime.datetime.now()
            errordict = str({"module":"calculator_func.py","function":"numbers_input()","Error":e,"date":date})
            errordict = error_source.err_source(e)
            error_log.create_log(errordict)
            return numbers_input()

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
    if second_num !=0:
        return first_num / second_num
    else:
        print("Second number should not be zero")
        first_num,second_num = numbers_input()
        return first_num / second_num
    
def main():    
    menu()
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
main()
