from python.Utils.file_io import file_io_obj
import sys
import os
sys.path.append(os.getcwd())


def input_number():
    try:
        numbers = int(input("Enter number: "))
        squared_numbers = numbers ** 2
        print("Squared number is: ", squared_numbers)
    except Exception as e:
        print("Number should be in digits")
        file_io_obj.update_errorslog(
            file_io_obj.get_errdetails(e), file_io_obj.error_path)

        input_number()


input_number()
