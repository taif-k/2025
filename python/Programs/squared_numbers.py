import error_source
import error_log

def input_number():
    try: 
        numbers = int(input("Enter number: "))
        squared_numbers = numbers ** 2
        print("Squared number is: ",squared_numbers)
    except Exception as e:
        print("Number should be in digits") 
        date = error_log.get_currentdate()
        errordict = str({"module":"squared_numbers.py","function":"input_number()","error":e,"errortime":date})
        errordict = error_source.err_source(e)
        error_log.create_log(errordict)
        input_number()
              
input_number()