from python.Utils.file_io import file_io_obj
import os
import sys
sys.path.append(os.getcwd())


class Number:
    def numbers_input(self):
        try:
            first_number = int(input("Enter First Number: "))
            second_number = int(input("Enter Second Number: "))
            return first_number, second_number
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))
            
number_obj = Number()
