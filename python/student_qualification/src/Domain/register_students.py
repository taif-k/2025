import json


class Registration:
    def __init__(self):
        pass

    def student_registration(self):
        self.studentlist = []
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

            self.studentlist.append(studentdata)
            print(json.dumps(self.studentlist, indent=4))


student_obj = Registration()
