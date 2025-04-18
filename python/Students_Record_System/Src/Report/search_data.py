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
        activedata = Report.active_student()
        print(json.dumps(activedata,indent=3))
        print("\n-----Above is the List of Active Students-----\n")

    elif ask_report == 2:
        inactivedata = Report.inactive_student()
        print(json.dumps(inactivedata,indent=3))
        print("\n-----Above is the List of Inactive Students-----\n")
        

 