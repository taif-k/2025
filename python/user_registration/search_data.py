import json

def get_data():
    search_email = input("Enter email to search: ")

    with open(r"D:\student_details\all_students.json", 'r') as file:

        data = json.load(file)
        for studentdict in data:
                if studentdict.get("email") == search_email:
                     print(studentdict)
                     break
        else:
             print("email not found")        
                    
                     

                

