
def student_id(studentdict):
    while True:
        studentdict["id"] = input("Enter id: ")
        if studentdict["id"].isdigit():
            studentdict["id"] = int(studentdict["id"])
            return studentdict["id"]
        else:
            print("Enter id in digits only")
