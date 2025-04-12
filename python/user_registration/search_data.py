import json
import student_register
import datetime

log_path = r"D:\Repositories\2025\python\user_registration\studenterror_log.txt"
path =  r"D:\Repositories\2025\python\user_registration\all_students.json" 

def search_menu():
    print("1- Search Email")
    print("2- Search name")
    print("3- Search contact")
    print("4- Search address")
    print("0 - Go Back")

def get_file():
    with open(path,"r") as file:
        jsondata = json.load(file)
        return jsondata
         
def get_data():
    try:
        while True:
            print()
            search_menu()
            search_option = input("Enter search option: ")
            if search_option.isdigit():
                search_option = int(search_option)
                if search_option == 1:
                    search_email = input("Enter email to search: ")
                    data = get_file()
                    ispresent = False
                    for studentdict in data:
                        for key,value in studentdict.items():
                            if key == "email":
                                if value == search_email.lower():
                                    ispresent = True
                                    print(studentdict)
                                    break

                    if ispresent == False:
                        print("Email not found")

                elif search_option == 2:
                    search_name = input("Enter name to search: ")
                    data = get_file()
                    ispresent = False
                    for studentdict in data:
                        for key,value in studentdict.items():
                            if key == "name":
                                if value == search_name.lower():
                                    ispresent = True
                                    print(studentdict)
                                    break

                    if ispresent == False:
                        print("name not found")   

                elif search_option == 3:
                    search_contact = int(input("Enter contact to search: "))
                    data = get_file()
                    ispresent = False
                    for studentdict in data:
                        for key,value in studentdict.items():
                            if key == "contact":
                                if value == search_contact:
                                    ispresent = True
                                    print(studentdict)
                                    break

                    if ispresent == False:
                        print("contact not found")                    

                elif search_option == 4:
                    search_address = input("Enter address to search: ")
                    data = get_file()
                    ispresent = False
                    for studentdict in data:
                        for key,value in studentdict.items():
                            if key == "address":
                                if value == search_address.lower():
                                    ispresent = True
                                    print(studentdict)
                                    break

                    if ispresent == False:
                        print("Address not found")
    
                elif search_option == 0:
                    break
                else:
                    print("Invalid option")
            else:
                print("Task number should be in digits")
    except Exception as e:
        print("Register students to search")
        date = datetime.datetime.now()
        errordetail = str({"module":"search_data.py","function":"get_data","error":e,"date":date})
        student_register.create_userfile(errordetail,log_path)
        return student_register.register_user() # if json file missing, Registration and json file will be created



