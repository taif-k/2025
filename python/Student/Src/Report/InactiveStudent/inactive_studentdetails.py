import Domain
import Search


log_path = r"D:\Repositories\2025\python\Student\Src\Database\errorslog.txt"

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
        date = Search.create_datetime()
        errordetails = str({"mod":"inactive_studentdetails.py","error":e,"date":date})
        Domain.update_errorlog(errordetails,log_path)