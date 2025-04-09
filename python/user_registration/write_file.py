import os

def create_userfile(studentdict,jsondata):
        path = r"D:\student_details"
        fpath = os.path.join(path,f"{studentdict["name"]}.json")
        with open(fpath,"w") as file:
            file.write(jsondata) 