
import random

def read_writefile():
    path = r"D:\multiplefolders\plus_mode.txt"
    var = random.randint(1,10)

    with open(path,"r+") as file:
        print(file.read())
        file.write(f"Appending data {var} ")
        print(file.read())
            
read_writefile()