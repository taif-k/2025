import sys
import os
sys.path.append(os.getcwd())

import python

datapath = r"D:\Repositories\2025\python\OOPS\Student_Records_System\Database\studentdata.json"
errorlog_path = r"D:\Repositories\2025\python\OOPS\Student_Records_System\Log\errorsdetail.txt"

student_one = python.student(datapath,errorlog_path)
student_one.menu_option()