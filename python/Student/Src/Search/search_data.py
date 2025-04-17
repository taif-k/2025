import json
import datetime
import Domain
import Report

records_path = r"C:\Users\DELL\Desktop\Src\Database\all_students.json"
log_path = r"C:\Users\DELL\Desktop\Src\Database\errorslog.txt"

def search_menu():
    print("1- Get Active Students")
    print("2- Get Inactive Students")
    print("0 - Go Back")

def create_datetime():
    date = datetime.datetime.now()
    shortdate = date.strftime("%d/%m/%Y, %H:%M:%S")
    return shortdate

def read_allrecords():  
    try:
        with open(records_path, "r") as file:
            data = json.load(file) # or data = json.loads(file.read()) 
        return data
    except Exception as e:
        print("Register students to search data")
        date = create_datetime()
        errordetail = str({"module":"search_data.py","function":"read_allrecords","error":e,"date":date})
        Domain.update_errorlog(errordetail,log_path)
        return []
        
def get_data():
    print("1  -  Active Students")
    print("2  -  Inactive Students")
    ask_report = int(input("Enter option: "))
    
    if ask_report == 1:
        activedata = Report.active_student()
        print(json.dumps(activedata,indent=3))

    elif ask_report == 2:
        inactivedata = Report.inactive_student()
        print(json.dumps(inactivedata,indent=3))
        

 