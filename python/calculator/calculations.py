# import inputnumbers
from python.calculator.inputnumbers import number_obj
from python.Utils.file_io import file_io_obj
import sys
import os
sys.path.append(os.getcwd())

class Calculation_operations:
    def addition(self):
        firstnum, secondnum = number_obj.numbers_input()
        add = firstnum + secondnum
        return add

    def divide(self):
        try:
            firstnum, secondnum = number_obj.numbers_input()
            div = firstnum / secondnum
            return div
        except Exception as e:
            print("Invalid Number")
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))
            return self.divide()

    def subtraction(self):
        firstnum, secondnum = number_obj.numbers_input()
        sub = firstnum - secondnum
        return sub

    def multiply(self):
        firstnum, secondnum = number_obj.numbers_input()
        mul = firstnum * secondnum
        return mul


cal_operartion_obj = Calculation_operations()
