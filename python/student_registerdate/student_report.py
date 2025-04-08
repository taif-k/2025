import datetime

def get_report(listdata):
    ask_month = int(input("Enter the month to filter students who joined in that month: "))
    get_students = []
    for studentdata in listdata:
        joined_date = datetime.datetime.strptime(studentdata["joineddate"], '%d-%m-%Y')
        if joined_date.month == ask_month:
            get_students.append(studentdata["name"])

    for name in get_students:
        print(f"Student joined in particular month",name)