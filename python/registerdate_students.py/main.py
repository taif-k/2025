import json
import datetime


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

    ask_month = int(input("Enter the month to filter students who joined in that month: "))
    get_students = []
    for studentdata in listdata:
        joined_date = datetime.datetime.strptime(studentdata["joineddate"], '%d-%m-%Y')
        if joined_date.month == ask_month:
            get_students.append(studentdata["name"])

    for name in get_students:
        print(name)

register_student()
