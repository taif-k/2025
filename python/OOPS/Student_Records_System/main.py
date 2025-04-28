import sys
import os
sys.path.append(os.getcwd())

import python as py_lang

datapath = r"D:\Repositories\2025\python\OOPS\Student_Records_System\Database\studentdata.json"
errorlog_path = r"D:\Repositories\2025\python\OOPS\Student_Records_System\Log\errorsdetail.txt"

student_one = py_lang.StudentMenu(datapath,errorlog_path)
student_one.menu_option()