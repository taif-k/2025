import json
from python.Utils.file_io import file_io_obj
from python.OOPS.Student_Records_System.Utils.read_writedata import file_obj
from python.OOPS.Student_Records_System.Domain.all_paths import paths_obj

class StudentSearch:
    def __init__(self,datapath):
        self.recordspath = datapath

    def search_student(self):
        try:
            search_name = input("Enter name to search: ")
            for data in file_obj.studentlist:
                if data["name"] == search_name:
                    print(json.dumps(data,indent=3))
                    print()
                    return None
            print("\nNot found")
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),paths_obj.err_log_path)