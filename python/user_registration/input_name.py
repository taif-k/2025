
def get_name(studentdict):
    while True:
        studentdict["name"] = input("Enter name: ")
        if studentdict["name"].isalpha():
            return studentdict["name"]
        else:
            print("name should not be in digits")