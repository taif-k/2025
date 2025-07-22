import traceback
import os
import datetime
import json
err_logpath = r"D:\Repositories\2025\python\Programs\errordetails.txt"

def error_details(e=None, get_onlydate = False):

    date = datetime.datetime.now()
    stringdate = date.strftime("%Y-%m-%d, %H:%M:%S") # keeping this format so that it match with datetime format(helpful in getting report)

    if get_onlydate == True:
        return stringdate
    
    if e is not None:
        tb = traceback.extract_tb(e.__traceback__)[-1]
        module_name = os.path.basename(tb.filename)
        function_name = tb.name
        lineno = tb.lineno

        # using dumps to get errors details in json double qoutes
        err_detail = json.dumps({"module": module_name,"function": function_name,"error": str(e),"date":stringdate,"line": lineno})

        # with str we're getting details in single qoute (which is not valid json format)
        # err_detail = str({"module": module_name,"function": function_name,"error": str(e),"date":stringdate,"line": lineno})
        return err_detail

def read_errors():
    with open(err_logpath,"r") as file:
        data = file.read()
        print(data)

def update_errorslog(data,path=err_logpath):
    with open(path,"a") as file:
        file.write(f"\n{data}") 
