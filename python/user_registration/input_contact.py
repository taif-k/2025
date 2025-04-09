

def get_contact(studentdict):
    while True:
        studentdict["contact"] = input("Enter contact: ")
        if studentdict["contact"].isdigit():
            studentdict["contact"] = int(studentdict["contact"])
            return studentdict["contact"]
        else:
            print("Contact should be in digits only")