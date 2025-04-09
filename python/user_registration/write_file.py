import os

def create_userfile(studentlist,jsondata):
        path = r"D:\student_details\all_students.json"
        with open(path,"w") as file:
            file.write(jsondata)