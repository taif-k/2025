
def student_register():
    studentlist = []
    for n in range(1,3):
        studentdict = {}
        
        studentdict["id"] = int(input("Enter id: "))
        studentdict["name"] = input("Enter name: ")
        studentdict["email"] = input("Enter email: ")
        studentdict["contact"] = int(input("Enter contact: "))
        studentlist.append(studentdict)
    return studentlist 