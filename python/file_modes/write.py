import os
path = r"D:\multiplefolders\taif.txt"

def write_file():
    if os.path.exists(path):
        print("File already exist, updating file")
    else:
        print("File not available, creating new file")

    with open(path,"w") as file:
        data = file.write("Overwritten text from write mode in existing file") # if path doesn't exist new file will be created

write_file()