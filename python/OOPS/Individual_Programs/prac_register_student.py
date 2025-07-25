import json
import sys,os
sys.path.append(os.getcwd())
from python.Utils.file_io import file_io_obj

class student:
    def __init__(self):
        self.ask_details()

    def ask_details(self):
        try:
            self.studentlist = []
            while True:
                self.name = input("Enter Name: ")
                self.age = int(input("Enter Age: "))
                self.grade = input("Enter Grade: ")
                studentdict = {}
                studentdict["name"] = self.name
                studentdict["age"] = self.age
                studentdict["grade"] = self.grade
                self.studentlist.append(studentdict)

                regsiter_student = input("Add More Students y/n: ")
                if regsiter_student == "y":
                    continue
                else:
                    break
            self.display_info()
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))

    def display_info(self):
        print(json.dumps(self.studentlist,indent=4))
        self.search_student()

    def search_student(self):
        search_name = input("Enter name to serach: ")
        isPresent = 0
        for data in self.studentlist:
            for key,value in data.items():
                if key == "name":
                    if value == search_name:
                        isPresent = 1
                        print(json.dumps(data,indent=3))
                        break

        if isPresent == 0:
            print("Not found")

studentdata = student()
