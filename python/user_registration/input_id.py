

def get_id(studentdict):
    while True:
        studentdict["id"] = input("Enter id: ")
        if studentdict["id"].isdigit():
            studentdict["id"] = int(studentdict["id"])
            return studentdict["id"]
        else:
            print("Id should be in digits only")