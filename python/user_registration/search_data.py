

def get_data(datalist):
    ispresent = False
    search_email = input("\nEnter email to search: ")
    for list in datalist:
        for key,value in list.items():
            if value == search_email:
                ispresent = True
                # print(list)
    if ispresent == True:
        print(list)     
    else:
        print("email not present")       
                

