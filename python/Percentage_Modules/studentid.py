import main

def student_id(studentdata):
    while True:
        studentdata["id"] = input("Enter id: ")
        if studentdata["id"].isdigit():
            return id
        else:
            print("Enter id in digits only")
