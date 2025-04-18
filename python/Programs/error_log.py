import datetime
path = r"D:\Repositories\2025\python\Programs\errordetails.txt"

def read_errors():
    with open(path,"r") as file:
        data = file.read()
        print(data)

def create_log(data):
    with open(path,"a") as file:
        file.write(f"\n{data}") 

def get_currentdate():
    date = datetime.datetime.now()
    short = date.strftime("%d/%m/%Y, %H:%M:%S")
    return get_currentdate