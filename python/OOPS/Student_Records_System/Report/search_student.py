import json
from python.OOPS.Student_Records_System.Utils.read_writedata import file_obj

class StudentSearch:
    def __init__(self,datapath):
        self.recordspath = datapath

    def search_student(self):
        search_name = input("Enter name to search: ")
        for data in file_obj.studentlist:
            if data["name"] == search_name:
                print(json.dumps(data,indent=3))
                print()
                return None
        print("\nNot found")