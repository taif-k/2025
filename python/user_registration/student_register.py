import json
import datetime

log_path = r"D:\Repositories\2025\python\user_registration\studenterror_log.txt"
path = r"D:\Repositories\2025\python\user_registration\all_students.json" 

def create_userfile(jsondata,path):
        with open(path,"a") as file:
            file.write(f"\n{jsondata}")

def read_alldata():
    try:
        with open(path, "r") as file:
            data = file.read()
            print(data)
    except Exception as e:
        print("Students data not available, Register to see data ")
        date = datetime.datetime.now()
        errordetails = str({"module":"student_regsiter.py","function":"read_alldata()","error":e,"date":date})
        create_userfile(errordetails,log_path)
        return register_user() # if json file missing, Registration and json file will be created

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
    studentlist = []
    for n in range(1,3):
        studentdict = {}
        studentdict["id"] = get_id(studentdict)
        studentdict["name"] = get_name(studentdict)
        studentdict["email"] = get_email(studentdict)
        studentdict["address"] = get_address(studentdict)
        studentdict["contact"] = get_contact(studentdict)
        date = datetime.datetime.now()
        studentdict["joneddate"] = date.strftime("%d/%m/%Y, %H:%M:%S")

        studentlist.append(studentdict)

    jsondata = json.dumps(studentlist,indent=3)
    create_userfile(jsondata,path) 