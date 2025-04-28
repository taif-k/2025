import json
import python as py_lang

datapath = r"D:\Repositories\2025\python\OOPS\Student_Records_System\Database\studentdata.json"
errorlog_path = r"D:\Repositories\2025\python\OOPS\Student_Records_System\Log\errorsdetail.txt"

class DataOperations:
        def __init__(self,datapath,errorlog_path):
            self.recordspath = datapath
            self.err_path = errorlog_path
            self.studentlist = self.read_alldata()

        def write_data(self):
            with open(self.recordspath,"w") as file:
                file.write(json.dumps(self.studentlist,indent=3))

        def read_alldata(self):
            try:
                with open(self.recordspath, "r") as file:
                    studentrecords = json.load(file)
                    return studentrecords
            except Exception as e:
                print("Student Records are blank")
                py_lang.update_errorslog(py_lang.error_details(e),self.err_path)
                return []   
            