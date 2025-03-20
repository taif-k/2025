studentdata = {}
qualificationdata = {}
listdata = []

studentdata["id"] = int(input("Enter student id: "))
studentdata["name"] = (input("Enter student name: "))
studentdata["qualification"] = listdata

qualificationdata["qualificationname"] = input("Enter 1st Qualification: ")
qualificationdata["passingyear"] = input("Enter passing year: ")
listdata.append(qualificationdata)

qualificationdata = {}

qualificationdata["qualificationname"] = input("Enter 2nd Qualification: ")
qualificationdata["passingyear"] = input("Enter passing year: ")
listdata.append(qualificationdata)

print(studentdata)

