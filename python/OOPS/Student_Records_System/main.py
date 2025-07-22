import sys
import os
sys.path.append(os.getcwd())

from python.OOPS.Student_Records_System.Domain.student_registration import StudentMenu
from python.OOPS.Student_Records_System.Domain.all_paths import paths_obj

student_obj = StudentMenu(paths_obj.datapath,paths_obj.errorlog_path)
student_obj.menu_option()