from python.OOPS.Library_Management_System.src.Domain.book_options import BookOption
from python.Utils.file_io import file_io_obj

bookdata = r"D:\Repositories\2025\python\OOPS\Library_Management_System\src\Database\bookdata.json"


class BookMenu(BookOption):
    def __init__(self, path):
        super().__init__(path)
        self.__pin = 123

    def menu(self):
        print()
        print("1- Add Book")
        print("2- Borrow Book")
        print("3- Return Book")
        print("4- Exit")

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
                    elif ask_option == 4:
                        break
            else:
                print("Incorrect pin")
        except Exception as e:
            print("Try Again after some time..")
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))


bookmenu_obj = BookMenu(bookdata)
