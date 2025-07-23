import sys,os
sys.path.append(os.getcwd())

from python.Utils.file_io import file_io_obj
from python.calculator.calculations import cal_operartion_obj

class Calculator:
    def menu_options(self):
        print("Press 1 for Addition")
        print("Press 2 for Subtraction")
        print("Press 3 for Multiplication")
        print("Press 4 for Division")
        print("Press 0 for Exit")


    def menu(self):
        self.menu_options()
        try:
            while True:
                menuinput = input("Enter Task no: ")
                if menuinput.isdigit():
                    menuinput = int(menuinput)
                    if menuinput == 1:
                        print("Addition is ", cal_operartion_obj.addition())
                    elif menuinput == 2:
                        print("Subtraction is", cal_operartion_obj.subtraction())
                    elif menuinput == 3:
                        print("Multiplication is", cal_operartion_obj.multiply())
                    elif menuinput == 4:
                        print("Division is", cal_operartion_obj.divide())
                    elif menuinput == 0:
                        break
                    else:
                        print("Choose valid option ")
                else:
                    print("Enter valid Task Number")
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))

Calculator_obj = Calculator() 
Calculator_obj.menu()
