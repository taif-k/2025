import error_source

def input_number():
    try: 
        numbers = int(input("Enter number: "))
        squared_numbers = numbers ** 2
        print("Squared number is: ",squared_numbers)
    except Exception as e:
        print("Number should be in digits")
        error_source.update_errorslog(error_source.error_details(e))
        input_number()
              
input_number()