import error_source

def input_details():

    try:
        userdict = {}
        userdict["name"] = "taif"
        userdict["accountno"] = 12345678901
        userdict["amount"] = int(input("Add amount: "))
        
        print(userdict) 
    except Exception as e:
        print("Unable to add money...")
        error_source.update_errorslog(error_source.error_details(e))    

input_details()
