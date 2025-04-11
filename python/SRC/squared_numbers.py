import datetime
import error_log

path = r"D:\Repositories\2025\python\SRC\errordetails.txt"

def input_number():
    try: 
        numbers = int(input("Enter number: "))
        squared_numbers = numbers ** 2
        print("Squared number is: ",squared_numbers)
    except Exception as e:
        print("Number should be in digits") 

        date = datetime.datetime.now()
        errordict = str({"module":"squared_numbers.py","function":"input_number()","error":e,"errortime":date})
        error_log.create_log(errordict)
        input_number()
              
input_number()