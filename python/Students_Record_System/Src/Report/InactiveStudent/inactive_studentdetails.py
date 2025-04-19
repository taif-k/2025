import Domain

def inactive_student():
    inactivelist = []
    data = Domain.studentlist
    for studentdict in data:
        for key,value in studentdict.items():
            if key == "isActive":
                if value == "False":
                    inactivelist.append(studentdict)
    return inactivelist

        