import os

def foldername(n):
    path = r"D:\multiplefolders" # change according to your desired path
    while True:
        user_input = input("Enter number of folders to make: ")     
        if user_input.isdigit():   
            user_input = int(user_input)    
            count = 0
            while count < user_input:
                folder_name = f"taif_{n}"
                folder_path = os.path.join(path, folder_name)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                    count += 1
                n += 2
            break        
        else:
            print("Enter valid number")        