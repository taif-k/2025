import Domain
import datetime
import json
import Report

records_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\all_students.json"
log_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\errorslog.txt"

def menu():
    print("1 - Student Registration")
    print("2 - Display All Records")
    print("3 - Get Report")
    print("0 - Exit")

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

def menu_option():
    print("\n----STUDENT RECORDS MANAGEMENT SYSTEM----\n")
    while True:
        menu()
        task_input = input("Enter Task number: ")
        if task_input.isdigit():
            task_input = int(task_input)
            if task_input == 1: 
                Domain.register_user()
            elif task_input == 2:
                pass
                data = read_allrecords()
                print(json.dumps(data,indent=4))
            elif task_input == 3:
                pass
                Report.get_data()
            elif task_input == 0:
                break
            else:
                print("Invalid option\n")
        else:
            print("Task number should be in digit only\n")     

if __name__ == "__main__":
    menu_option()
 
            
