import Domain

def inactive_student():
    inactivelist = []
    data = Domain.studentlist
    
    if not data:
        return "Data not available for Search....Register Students please"
    
    for studentdict in data:
        for key,value in studentdict.items():
            if key == "isActive":
                if value == "False":
                    inactivelist.append(studentdict)
    return inactivelist

        