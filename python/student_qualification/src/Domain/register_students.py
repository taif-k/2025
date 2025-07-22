import json

def student_registration():
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