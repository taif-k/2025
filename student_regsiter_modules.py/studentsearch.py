def student_search(data):
    search_name = input("Enter name to search: ")
    ispresent = False
    for dict in data:
        if dict["name"] == search_name:
            ispresent = True
            print(dict)

    if ispresent == False:
        print("Not found") 