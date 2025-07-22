import json
from python.Programs.error_source import error_details,update_errorslog
from python.student_qualification.src.Domain.paths import diff_path_obj

class Registration:
    def __init__(self):
        pass

    def student_registration(self):
        try:
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
        except Exception as e:
            update_errorslog(error_details(e),diff_path_obj.errorlog_path)

student_obj = Registration()
