
import write_file
import json
import input_id
import input_name
import input_contact
import input_email
import datetime
import input_address

def register_user():
    studentlist = []
    for n in range(1,3):
        studentdict = {} 
        input_id.get_id(studentdict)
        input_name.get_name(studentdict)
        input_address.get_address(studentdict)
        input_email.get_email(studentdict)
        input_contact.get_contact(studentdict)
        date = datetime.datetime.now()
        studentdict["joneddate"] = date.strftime("%d/%m/%Y, %H:%M:%S")

        studentlist.append(studentdict)

    jsondata = json.dumps(studentlist,indent=3)
    write_file.create_userfile(studentlist,jsondata)
    return studentlist    