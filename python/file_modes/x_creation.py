path = r"D:\multiplefolders\exclusive_create.txt"

def exclusive_creation():
    with open(path,"x") as file:
        new_data = file.write("Creating a new file using x mode")

exclusive_creation()