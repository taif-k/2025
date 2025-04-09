
path = r"D:\multiplefolders\taif.txt"

def append_data():
    with open(path,"a") as file:
        new_data = file.write(", Appending new data with old data or create new file using append mode also")

append_data()