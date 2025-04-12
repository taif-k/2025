<<<<<<< HEAD
import datetime
=======
import error_source
>>>>>>> 7959194c4f8b6bfae647041d94a7f9f60580ce6b
import error_log

path = r"D:\Repositories\2025\python\SRC\errordetails.txt"

def input_number():
    try: 
        numbers = int(input("Enter number: "))
        squared_numbers = numbers ** 2
        print("Squared number is: ",squared_numbers)
    except Exception as e:
        print("Number should be in digits") 

<<<<<<< HEAD
        date = datetime.datetime.now()
        errordict = str({"module":"squared_numbers.py","function":"input_number()","error":e,"errortime":date})
=======
        errordict = error_source.err_source(e)
>>>>>>> 7959194c4f8b6bfae647041d94a7f9f60580ce6b
        error_log.create_log(errordict)
        input_number()
              
input_number()