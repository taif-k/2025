import json
import Report

def search_menu():
    print("1- Get Active Students")
    print("2- Get Inactive Students")
    print("0 - Go Back")

def get_data():
    print("1  -  Active Students")
    print("2  -  Inactive Students")
    ask_report = int(input("Enter option: "))
    
    if ask_report == 1:
        data = Report.active_student()

    elif ask_report == 2:
        data = Report.inactive_student()

    else:
        data = None
        print("Invalid option")    

    if data:
        print(json.dumps(data,indent=3)) 
        

 