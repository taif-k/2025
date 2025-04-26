import json
jsonpath = r"D:\Repositories\2025\python\OOPS\Library_Management_System\bookdata.json"

class Book:
    def __init__(self,path):
        self.jsonpath = path
        self.booklist = self.read_bookdata()

    def write_data(self):
        with open(self.jsonpath,"w") as file:
            file.write(json.dumps(self.booklist,indent=4))

    def read_bookdata(self):
        try:
            with open(self.jsonpath,"r") as file:
                data = json.load(file)
                return data
        except Exception as e:
            return [] 

class AddBook(Book):
    def __init__(self, path):
        Book.__init__(self,path)

    def add_book(self):
        while True:
            ask_addbook = input("Want to add a new book y/n: ")
            if ask_addbook.lower() == "y":
                self.enter_book = input("Enter Book name to Add: ").lower()
                self.author_name = input("Enter Author name: ")

                alreadypresent = False
                for bookdict in self.booklist:
                    if bookdict["book_name"].lower() == self.enter_book:
                        alreadypresent = True
                        break

                if alreadypresent == True:
                    print("Already added in database")
                    continue

                bookdict = {"book_name":self.enter_book,"author_name":self.author_name}
                self.booklist.append(bookdict)
                self.write_data()
            elif ask_addbook.lower() == "n":
                break
 
class BorrowBook(AddBook):
    def __init__(self,path):
        AddBook.__init__(self,path)

    def borrow_book(self):
        already_borrow = 0
        self.enter_book = input("Enter book name to borrow: ").lower()
        for bookdict in self.booklist:
            for key,value in bookdict.items():
                if key == "book_name":
                    if value.lower() == self.enter_book:
                        self.booklist.remove(bookdict)                        
                        self.write_data()
                        print("Book Borrowed")
                        already_borrow = 1
                        break

        if already_borrow == 0:
            print("Book not found")


class ReturnBook(BorrowBook):
    def __init__(self,path):
        BorrowBook.__init__(self,path)

    def return_book(self):
        self.enter_book  = input("Enter book name To Return: ").lower()
        already_return = 0 
        for bookdict in self.booklist:
            for key,value in bookdict.items():
                if key == "book_name":
                    if value.lower() == self.enter_book:
                        print("Book already present in database")
                        already_return = 1
                        break

        if already_return == 0:
            self.add_book()
            print("Book Returned ")


class BookMenu(ReturnBook): #
    def __init__(self,path):
        ReturnBook.__init__(self,path)
        self.__pin = 123

    def menu(self):
        print()
        print("1- Add Book")
        print("2- Borrow Book")
        print("3- Return Book")
        print("4- See All Books")
        print("5- Exit")

    def menu_option(self):
        print("\n---Library Management System---\n")
        try:
            verify_pin = int(input("Enter pin to proceed: "))
            if verify_pin == self.__pin:
                while True:
                    self.menu()
                    ask_option = int(input("\nEnter option: "))
                    if ask_option == 1:
                        self.add_book()
                    elif ask_option == 2:
                        self.borrow_book()
                    elif ask_option == 3:
                        self.return_book()
                        pass
                    elif ask_option == 4:
                        print(json.dumps(self.booklist,indent=4))
                    elif ask_option == 5:
                        break
            else:
                print("Incorrect pin")     
        except:
            print("Enter correct details..")

book_one = BookMenu(jsonpath)
book_one.menu_option()