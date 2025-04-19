import json
import sys,os
sys.path.append(os.getcwd())
from python import error_details,update_errorslog
path = r"D:\Repositories\2025\python\user_registration\all_students.json" 
err_log = r"D:\Repositories\2025\python\user_registration\studenterror_log.txt"

def create_userfile(jsondata,path):
        with open(path,"w") as file:
            file.write(f"\n{jsondata}")

def read_alldata():
    try:
        with open(path, "r") as file:
            data = json.load(file)
            return data
    except:
        print("Students data not available, Register to see data ")
        return []

def get_address():
    while True:
        ask_address = input("Enter address: ")
        if ask_address.isdigit():
            continue
        else:
            return ask_address

def get_email():
    ask_email = input("Enter email: ")
    return ask_email

def get_id():
    try:
        while True:
            ask_id = int(input("Enter id : "))
            return ask_id
    except Exception as e:
        print("ID should be only digits ")
        update_errorslog(error_details(e),err_log)
        return get_id()

def get_contact():
    while True:
        ask_contact = input("Enter contact: ")
        if ask_contact.isdigit():
            ask_contact = int(input("Enter contact"))
            return ask_contact
        else:
            print("Contact should be in digits only")

def get_name():
    while True:
        ask_name = input("Enter name: ")
        if ask_name.isalpha():
            return ask_name
        else:
            print("Name should be in alphabets")

def register_user():
    studentlist = read_alldata()
    studentdict = {}
    studentdict["id"] = get_id()
    studentdict["name"] = get_name()
    studentdict["email"] = get_email()
    studentdict["address"] = get_address()
    studentdict["contact"] = get_contact()
    studentdict["joineddate"] = error_details(get_onlydate=True)

    studentlist.append(studentdict)

    jsondata = json.dumps(studentlist,indent=3)
    create_userfile(jsondata,path) 
    print("Registered sucessfully...")