import datetime
err_logpath = r"D:\Repositories\2025\python\Programs\errordetails.txt"

def read_errors():
    with open(err_logpath,"r") as file:
        data = file.read()
        print(data)

def create_log(data):
    with open(err_logpath,"a") as file:
        file.write(f"\n{data}") 

def get_currentdate():
    date = datetime.datetime.now()
    shortdate = date.strftime("%d/%m/%Y, %H:%M:%S")
    return shortdate