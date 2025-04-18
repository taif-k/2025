import Domain
log_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\errorslog.txt"

def active_student():
    try:
        activelist = []
        data = Domain.studentlist
        for studentdict in data:
            for key,value in studentdict.items():
                if key == "isActive":
                    if value == "True":
                        activelist.append(studentdict)

        return activelist
    
    except Exception as e:
        date = Domain.create_datetime()
        errordeatils = str({"mod":"active_studentdetails.py","error":e,"date":date})
        Domain.update_errorlog(errordeatils,log_path)
        