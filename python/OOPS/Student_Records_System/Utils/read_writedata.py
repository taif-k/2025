import json
from python.Programs.error_source import update_errorslog,error_details

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
                update_errorslog(error_details(e),self.err_path)
                return []   
            