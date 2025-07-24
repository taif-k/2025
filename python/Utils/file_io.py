import json
import datetime
import traceback
import os
from python.web_scrap_concepts.src.Domain.scrap_paths import path_obj
error_path = r"D:\Repositories\2025\python\Log\error_log.txt"


class FileIO:
    def __init__(self, error_path):
        self.error_path = error_path

    # storing data in local files 
    def write_data(self, data, path):
        with open(path, "w") as file:
            file.write(json.dumps(data, indent=4))

    # logging errors details
    def update_errorslog(self, data, path=error_path):
        if path == path_obj.program_run_capture:
            write_arg = f"\nProgram ran at {data}"
        else:
            write_arg = f"\n{data}"

        with open(path, "a") as file:
            file.write(write_arg)


    # read file data
    def read_alldata(self, path):
        try:
            with open(path, "r") as file:
                data = json.load(file)
                return data
        except Exception as e:
            print("check error log..")
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))
            return []
        
    # traceback module to get dyn. err details
    def get_errdetails(self, error=None, get_date=False):
        date = datetime.datetime.now()
        str_date = date.strftime("%Y-%m-%d %H:%M:%S")

        if get_date == True:
            return str_date

        if error is not None:
            tb = traceback.extract_tb(error.__traceback__)[-1]
            module_name = os.path.basename(tb.filename)
            function_name = tb.name
            line_no = tb.lineno

            err_details = json.dumps({"module": module_name, "function": function_name, "error": str(
                error), "date": str_date, "line": line_no})
            return err_details


file_io_obj = FileIO(error_path)
