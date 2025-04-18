import Domain
import Search


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
        date = Search.create_datetime()
        errordeatils = str({"mod":"active_studentdetails.py","error":e,"date":date})
        path = Search.log_path
        Domain.update_errorlog(errordeatils,path)
        