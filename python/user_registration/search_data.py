import json
import student_register
import sys
import os
sys.path.append(os.getcwd())
from python import get_currentdate,create_log

path =  r"D:\Repositories\2025\python\user_registration\all_students.json" 

def search_menu():
    print("1- Search Email")
    print("2- Search contact")
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
    
                elif search_option == 0:
                    break
                else:
                    print("Invalid option")
            else:
                print("Task number should be in digits")
    except Exception as e:
        print("Register students to search")
        date = get_currentdate()
        errordetail = str({"module":"search_data.py","function":"get_data","error":e,"date":date})
        create_log(errordetail)
        return student_register.register_user() # if json file missing, Registration and json file will be created
