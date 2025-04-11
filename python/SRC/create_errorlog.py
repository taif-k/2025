path = r"D:\Repositories\2025\python\SRC\errordetails.txt"

def create_log(error):
    with open(path,"a") as file:
        file.write(f"\n{error}") #
