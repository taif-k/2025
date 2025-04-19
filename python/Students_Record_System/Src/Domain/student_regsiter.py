import json
import Domain
import sys,os
sys.path.append(os.getcwd())
import python

records_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\all_students.json"
log_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\errorslog.txt"

def write_data(data,path):
    with open(path,"w") as file:
        file.write(f"\n{data}")

def update_errorlog(errordata,log_path):
    with open(log_path,"a") as file:
        file.write(f"\n{errordata}")

def read_allrecords(path = records_path):  
    try:
        with open(path, "r") as file:
            data = json.load(file) # or data = json.loads(file.read()) 
        return data
    except Exception as e:
        print("Register students to search data")
        Domain.update_errorlog(python.error_details(e),log_path)
        return []

def get_status():
    ask_status = input("Is student Active: t/f: ")
    if ask_status.lower() == "t".lower():
        isActive = "True"
        return isActive 
    elif ask_status.lower() == "f".lower():
        isActive = "False"
        return isActive

def get_address():
    while True:
        input_address = input("Enter address: ")
        if input_address.isdigit():
            print("Address cannot be only digits")
        else:
            return input_address

def get_email():
        input_email = input("Enter email: ")
        if input_email.isdigit():
            print("Invalid email")
        else:
            return input_email

def get_id():
    while True:
        input_id = input("Enter id: ")
        if input_id.isdigit():
            input_id = int(input_id)
            return input_id
        else:
            print("Id should be in digits only")

def get_contact():
    while True:
        input_contact = input("Enter contact: ")
        if input_contact.isdigit():
            if len(input_contact) == 10:
                input_contact = int(input_contact)
                return input_contact
            else:
                print("Contact should be 10 digits")
        else:
            print("Contact should be only digits")

def get_name():
    while True:
        input_name = input("Enter name: ")
        if input_name.isalpha():
            return input_name
        else:
            print("Invalid name")

def get_qualification():
    try:
        qualificationlist = []
        while True:
            qualificationdict = {}
            ask_qualification = input("Add Qualifications: y/n ")
            
            if ask_qualification.lower() == "y" :
                qualification_name = input("Enter qualification: ")
                qualificationdict["qualification_name"] = qualification_name
                qualificationdict["passing_year"] = int(input("Enter passing year: "))

                same_qualification = False
                for qualification in qualificationlist:
                    if qualification["qualification_name"].lower() == qualification_name.lower():
                        same_qualification = True
                        break

                if same_qualification == True:
                    print("Qualification already added")    
                    continue 

                qualificationlist.append(qualificationdict)
                print("Qualification added...want to different qualification")

            elif ask_qualification.lower() == "n":
                break
            else:
                print("Choose y/n")
        return qualificationlist 
            
    except Exception as e:                   
        print("Enter correct detail..")
        update_errorlog(python.error_details(e),log_path)
        return get_qualification()
    
studentlist = read_allrecords()
def register_user():
    studentdict = {}
    studentdict["id"] = get_id()
    studentdict["name"] = get_name()
    studentdict["qualification"] = get_qualification()
    studentdict["email"] = get_email()
    studentdict["address"] = get_address()
    studentdict["contact"] = get_contact()
    studentdict["isActive"] = get_status()
    studentdict["joneddate"] = python.error_details(get_onlydate=True)

    studentlist.append(studentdict)

    json_string = json.dumps(studentlist,indent=3)
    write_data(json_string,records_path)
    print("\nStudent register Sucessfully...")