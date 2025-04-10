
import json
import datetime

def create_userfile(jsondata):
        path = r"D:\student_details\all_students.json"
        with open(path,"w") as file:
            file.write(jsondata)

def read_allfiles():
    path = r"D:\student_details\all_students.json"
    with open(path, "r") as file:
        data = file.read()
        print(data)

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
    for n in range(1,6):
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
    create_userfile(jsondata)
    return studentlist    