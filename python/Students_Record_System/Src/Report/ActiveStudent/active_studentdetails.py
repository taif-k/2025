import Domain
import datetime
log_path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\errorslog.txt"

def create_datetime():
    date = datetime.datetime.now()
    shortdate = date.strftime("%d/%m/%Y, %H:%M:%S")
    return shortdate

def active_student():
    #print(Domain.studentlist)
    try:
        activelist = []
        data = Domain.studentlist
        for studentdict in data:
            for key,value in studentdict.items():
                if key == "isActive":
                    if value == "True":
                        activelist.append(studentdict)

        return activelist
        #print(activelist)
    except Exception as e:
        date = create_datetime()
        errordeatils = str({"mod":"active_studentdetails.py","error":e,"date":date})
        Domain.update_errorlog(errordeatils,log_path)
        