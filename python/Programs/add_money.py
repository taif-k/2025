import error_log
import datetime


def input_details():

    try:
        userdict = {}
        userdict["name"] = "taif"
        userdict["accountno"] = 12345678901

        userdict["amount"] = int(input("Add amount: "))
        print(userdict) 
    except Exception as e:
        print("Unable to add money...")
        date = datetime.datetime.now()
        errordetails = str({"module":"add_money.py","function":"input_details","error":e,"date":date})
        error_log.create_log(errordetails)    

input_details()