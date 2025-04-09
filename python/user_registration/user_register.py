
import write_file
import json
import input_id
import input_name
import input_contact
import input_email

def register_user():
    studentlist = []
    for n in range(1,3):
        studentdict = {} 

        input_id.get_id(studentdict)
        input_name.get_name(studentdict)
        input_contact.get_contact(studentdict)
        input_email.get_email(studentdict)

        studentlist.append(studentdict)
        jsondata = json.dumps(studentdict,indent=3)

        write_file.create_userfile(studentdict,jsondata)
    print(json.dumps(studentlist,indent=3))   