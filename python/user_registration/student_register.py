import json
import sys,os
sys.path.append(os.getcwd())
from python import error_details
path = r"D:\Repositories\2025\python\user_registration\all_students.json" 

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

def get_address(studentdict):
    while True:
        studentdict["address"] = input("Enter address: ")
        return studentdict["address"]

def get_email(studentdict):
        studentdict["email"] = input("Enter email: ")
        return studentdict["email"]

def get_id(studentdict):
    while True:
        studentdict["id"] = input("Enter id: ")
        if studentdict["id"].isdigit():
            studentdict["id"] = int(studentdict["id"])
            return studentdict["id"]
        else:
            print("Id should be in digits only")

def get_contact(studentdict):
    while True:
        studentdict["contact"] = input("Enter contact: ")
        if studentdict["contact"].isdigit():
            studentdict["contact"] = int(studentdict["contact"])
            return studentdict["contact"]
        else:
            print("Contact should be in digits only")

def get_name(studentdict):
    while True:
        studentdict["name"] = input("Enter name: ")
        if studentdict["name"].isalpha():
            return studentdict["name"]
        else:
            print("name should not be in digits")

def register_user():
    studentlist = read_alldata()
    studentdict = {}
    studentdict["id"] = get_id(studentdict)
    studentdict["name"] = get_name(studentdict)
    studentdict["email"] = get_email(studentdict)
    studentdict["address"] = get_address(studentdict)
    studentdict["contact"] = get_contact(studentdict)
    studentdict["joineddate"] = error_details(get_onlydate=True)

    studentlist.append(studentdict)

    jsondata = json.dumps(studentlist,indent=3)
    create_userfile(jsondata,path) 
    print("Registered sucessfully...")