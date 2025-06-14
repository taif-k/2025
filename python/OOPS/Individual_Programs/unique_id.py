import uuid
import json

class User:
    def __init__(self):
        self.registration()

    def registration(self):
        self.unique_id = str(uuid.uuid4())[:5]
        self.userdict = {}
        self.userdict["name"] = input("Enter name: ")
        self.userdict["contact"] = int(input("Enter contact: "))
        self.userdict["user_id"] = self.userdict["name"]+ "_" + self.unique_id
        print(json.dumps(self.userdict,indent=3))

obj = User()
