import json

def get_data():
    search_email = input("Enter email to search: ")

    with open(r"D:\student_details\all_students.json", 'r') as file:
        data = json.load(file)
        ispresent = False
        for studentdict in data:
            for key,value in studentdict.items():
                if key == "email":
                    if value == search_email:
                        print(studentdict)

        if ispresent == False:
            print("email Not found")

