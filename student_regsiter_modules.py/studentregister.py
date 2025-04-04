
def student_register():
    studentlist = []
    for n in range(1,3):
        studentdict = {}
        count = 0        
        while count <1:                
            studentdict["id"] = input("Enter id: ")
            if studentdict["id"].isdigit():
                studentdict["id"] = int(studentdict["id"])
                while count <1:
                    studentdict["name"] = input("Enter name: ")
                    if studentdict["name"].isalpha():
                            studentdict["email"] = input("Enter email: ")
                            while count <1:
                                    studentdict["contact"] = input("Enter contact: ")
                                    if studentdict["contact"].isdigit():
                                        count = 1
                                    else:
                                        print("Contact should be in digits only")
                    else:
                        print("Name should be in alphabets only")
            else:
                print("Id should be in digit")
            studentlist.append(studentdict)
    return studentlist 