
paths = [r"D:\multiplefolders\taif.txt",r"D:\Repositories\2025\python\file_modes\read.py"] #change accordingly

def path_input():
    path_input = int(input("Enter path number (start from 0): "))
    if path_input == 0:
        n = path_input
        read_file(n)
    elif path_input == 1:
        n = path_input
        read_file(n)

def read_file(n):
    with open(paths[n],"r") as file:
        data = file.read()
        print(data)

path_input()