
def input_name(studentdict):
        while True:
            studentdict["name"] = input("Enter name: ")
            if studentdict["name"].isalpha():
                return studentdict["name"]
            else:
                print("Name should be in alphabets only")
    

        