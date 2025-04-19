import Domain
import sys,os
sys.path.append(os.getcwd())
import python
log_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\errorslog.txt"

def inactive_student():
    try:
        inactivelist = []
        data = Domain.studentlist
        for studentdict in data:
            for key,value in studentdict.items():
                if key == "isActive":
                    if value == "False":
                        inactivelist.append(studentdict)
        return inactivelist
    
    except Exception as e:
        Domain.update_errorlog(python.error_details(e),log_path)