import datetime

path = r"D:\Repositories\2025\python\SRC\errordetails.txt"

def errorlog(error):
    with open(path,"a") as file:
        file.write(f"\n{error}") #

def input_number():
    try: 
        numbers = int(input("Enter number: "))
        squared_numbers = numbers ** 2
        print("Squared number is: ",squared_numbers)
    except Exception as e:
        print("Number should be in digits") 

        date = datetime.datetime.now()
        errordict = str({"function":"input_number()","error":e,"errortime":date})
        errorlog(errordict)
        input_number()
              
input_number()