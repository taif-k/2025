import Domain

def active_student():
    activelist = []
    data = Domain.studentlist
    for studentdict in data:
        for key,value in studentdict.items():
            if key == "isActive":
                if value == "True":
                    activelist.append(studentdict)

    return activelist

        