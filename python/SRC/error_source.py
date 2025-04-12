import inspect
import os
import datetime

def err_source(e):

    frame = inspect.currentframe()
    module_name = os.path.basename(__file__)
    function_name = inspect.getframeinfo(frame).function
    date = datetime.datetime.now()
    lineno = inspect.getframeinfo(frame).lineno

    detail = str({"module": module_name,"function": function_name,"error": str(e),"date": date,"line":lineno})
    return detail
