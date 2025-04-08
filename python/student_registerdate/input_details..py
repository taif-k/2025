import json
import datetime
import student_report

def register_student():
    listdata = []
    for num in range(1, 3):
        studentdata = {}

        studentdata["id"] = input("Enter id: ")
        studentdata["name"] = input(f"Enter name {num}: ")
        joined_month = int(input("Enter joining month: "))
        joined_day = int(input("Enter joining day: "))
        current_date = datetime.datetime(2025, joined_month, joined_day)
        studentdata["joineddate"] = current_date.strftime('%d-%m-%Y')

        listdata.append(studentdata)
    print(json.dumps(listdata, indent=3))    
    student_report.get_report(listdata)

    

register_student()
