def student_search(data):
    while True:
        search_name = input("Enter name to search: ")
        if search_name.isalpha():
            ispresent = False
            for dict in data:
                if dict["name"] == search_name:
                    ispresent = True
                    print(dict)
            if ispresent == False:
                print("Not found") 
        else:
            print("Name should be in alphabets only")
        break