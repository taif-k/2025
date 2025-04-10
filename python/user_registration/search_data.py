import json

def get_data():
    search_email = input("Enter email to search: ")

    with open(r"D:\student_details\all_students.json", 'r') as file: # update path accordingly to avoid error
        data = json.load(file)
        ispresent = False
        for studentdict in data:
            for key,value in studentdict.items():
                if key == "email":
                    if value == search_email:
                        ispresent = True
                        print(studentdict)
                        break

        if ispresent == False:
            print("Email not found")
