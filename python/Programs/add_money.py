import sys,os
sys.path.append(os.getcwd())
from python.Utils.file_io import file_io_obj

def input_details():

    try:
        userdict = {}
        userdict["name"] = "taif"
        userdict["accountno"] = 12345678901
        userdict["amount"] = int(input("Add amount: "))
        
        print(userdict) 
    except Exception as e:
        print("Unable to add money...")
        file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),file_io_obj.error_path)

input_details()