import Domain
import datetime
log_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\errorslog.txt"

def create_datetime():
    date = datetime.datetime.now()
    shortdate = date.strftime("%d/%m/%Y, %H:%M:%S")
    return shortdate

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
        date = create_datetime()
        errordetails = str({"mod":"inactive_studentdetails.py","error":e,"date":date})
        Domain.update_errorlog(errordetails,log_path)