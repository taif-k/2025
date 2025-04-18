import json
import Search

records_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\all_students.json"
log_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\errorslog.txt"

def write_data(data,path):
    with open(path,"w") as file:
        file.write(f"\n{data}")

def update_errorlog(errordata,log_path):
    with open(log_path,"a") as file:
        file.write(f"\n{errordata}")


def get_status():
    ask_status = input("Is student Active: T/F: ")
    if ask_status.lower() == "t":
        isActive = "True"
        return isActive 
    elif ask_status.lower() == "f":
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
        date = Search.create_datetime()
        errordetails = str({"module":"student_register.py","function":"get_qualification","error":e,"date":date})
        update_errorlog(errordetails,log_path)
        return get_qualification()
    
studentlist = Search.read_allrecords()
def register_user():

    # will return [] if no data present
    studentdict = {}

    studentdict["id"] = get_id()
    studentdict["name"] = get_name()
    studentdict["qualification"] = get_qualification()
    studentdict["email"] = get_email()
    studentdict["address"] = get_address()
    studentdict["contact"] = get_contact()
    studentdict["status"] = get_status()
    studentdict["joneddate"] = Search.create_datetime()

    studentlist.append(studentdict)

    json_string = json.dumps(studentlist,indent=3)
    write_data(json_string,records_path)
    print("\nStudent register Sucessfully...")