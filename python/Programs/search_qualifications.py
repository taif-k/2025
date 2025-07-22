import json

studentlist = []
for num in range(1, 4):
    studentdata = {}
    qualificationlist = []
    studentdata["id"] = num
    studentdata["name"] = input("Enter name: ")
    studentdata["qualification"] = qualificationlist

    while True:
        qualificationdict = {}
        qualificationdict["qname"] = input("Enter qualification: ")
        qualificationdict["passingyear"] = input("Enter passing year")
        qualificationlist.append(qualificationdict)

        ask_qualification = input("Add More qualification - y or n: ")

        if ask_qualification.lower() != "y":
            break

    studentlist.append(studentdata)

print(json.dumps(studentlist, indent=4))

while True:
    qualification_search = input("Enter qualification to search: ")

    if qualification_search.isalnum():
        ispresent = False

        for single_student_dict in studentlist:
            for each_qualification_dict in single_student_dict["qualification"]:
                if qualification_search.lower() == each_qualification_dict["qname"].lower():
                    print(f"Student Name: {single_student_dict["name"]}")
                    ispresent = True
        if ispresent == False:
            print("qualification not found")
        break
    else:
        print("Enter valid qualification: ")
