import json
import datetime
import traceback
import os

error_path = r"D:\Repositories\2025\python\Log\error_log.txt"

class FileIO:        
    # def write_data(data, path):
    #     with open(path, "w") as file:
    #         file.write(f"\n{data}")

    # def write_data(self):
    #     with open(self.jsonpath, "w") as file:
    #         file.write(json.dumps(self.booklist, indent=4))
    def __init__(self,error_path):
        self.error_path = error_path

    def update_errorslog(self,data):
        with open(self.error_path, "a") as file:
            file.write(f"\n{data}")    

    # def write_data(self):
    #     with open(self.recordspath, "w") as file:
    #         file.write(json.dumps(self.studentlist, indent=3))

    # def read_allrecords(path=records_path):
    #     try:
    #         with open(path, "r") as file:
    #             data = json.load(file)  # or data = json.loads(file.read())
    #         return data
    #     except Exception as e:
    #         print("Register students to search data")
    #         python.update_errorslog(python.error_details(e), log_path)
    #         return []


    # def read_alldata(self):
    #     try:
    #         with open(self.recordspath, "r") as file:
    #             studentrecords = json.load(file)
    #             return studentrecords
    #     except Exception as e:
    #         print("Student Records are blank")
    #         update_errorslog(error_details(e), self.err_path)
    #         return []

        # def read_errors():
    #     with open(err_logpath, "r") as file:
    #         data = file.read()
    #         print(data)

    # def read_bookdata(self):
    #     try:
    #         with open(self.jsonpath, "r") as file:
    #             data = json.load(file)
    #             return data
    #     except:
    #         print("Book data unavailable")
    #         return []

    def get_errdetails(self,error = None, get_date = False):
        date = datetime.datetime.now()
        str_date = date.strftime("%Y-%m-%d %H:%M:%S")

        if get_date == True:
            return str_date
        
        if error is not None:
            tb = traceback.extract_tb(error.__traceback__)[-1]
            module_name = os.path.basename(tb.filename)
            function_name = tb.name
            line_no = tb.lineno

            err_details = json.dumps({"module":module_name,"function":function_name,"error":str(error),"date":str_date,"line":line_no})
            return err_details


file_io_obj = FileIO(error_path)
