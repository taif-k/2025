import json
import python as py_lang

class StudentSearch:
    def __init__(self,datapath,errorlog_path):
        self.recordspath = datapath
        self.err_path = errorlog_path

    def search_student(self):
        search_name = input("Enter name to search: ")
        listobj = py_lang.Student(self.recordspath, self.err_path)
        for data in listobj.studentlist:
            if data["name"] == search_name:
                print(json.dumps(data,indent=3))
                print()
                return None
        print("\nNot found")