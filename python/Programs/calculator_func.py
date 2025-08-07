import sys,os
sys.path.append(os.getcwd())
from python.Utils.file_io import file_io_obj

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
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),file_io_obj.error_path)
            print("Numbers should be in digits only")    
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
    try:
        first_num,second_num = numbers_input()
        return first_num / second_num
    except Exception as e:
        print("Second Number(Denominator) should not be zero")
        file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),file_io_obj.error_path)
        return division()
    
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
