
path = r"D:\Repositories\2025\python\SRC\errordetails.txt"

def read_errors():
    with open(path,"r") as file:
        data = file.read()
        print(data)

def create_log(error):
    with open(path,"a") as file:
        file.write(f"\n{error}") 