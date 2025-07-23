import json
import uuid
from python.Utils.file_io import file_io_obj


class Book:
    def __init__(self, path):
        self.jsonpath = path
        self.booklist = self.read_bookdata()
        self.borrowed_book = []

    def write_data(self):
        with open(self.jsonpath, "w") as file:
            file.write(json.dumps(self.booklist, indent=4))

    def read_bookdata(self):
        try:
            with open(self.jsonpath, "r") as file:
                data = json.load(file)
                return data
        except Exception as e:
            print("Book data unavailable")
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))
            return []


class BookOption(Book):
    def __init__(self, path):
        super().__init__(path)

    def add_book(self):
        try:
            while True:
                ask_addbook = input("Want to add a new book y/n: ")
                if ask_addbook.lower() == "y":
                    enter_book = input("Enter Book name to Add: ").lower()
                    author_name = input("Enter Author name: ")
                    book_id = str(uuid.uuid4())[:5]
                    if all(word.isalnum() for word in author_name.split()):
                        alreadypresent = False
                        for bookdict in self.booklist:
                            if bookdict["book_name"].lower() == enter_book:
                                alreadypresent = True
                                break

                        if alreadypresent == True:
                            print("Already added in database")
                            continue

                        bookdict = {"book_name": enter_book,
                                    "author_name": author_name, "book_id": book_id}
                        self.booklist.append(bookdict)
                        self.write_data()
                    else:
                        print("Author Name should be in Alphabets")
                elif ask_addbook.lower() == "n":
                    break
                else:
                    print("Choose either y or n")
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))

    def borrow_book(self):
        try:
            enter_book = input("Enter book name to borrow: ").lower()
            for bookdict in self.booklist:
                if bookdict["book_name"].lower() == enter_book:
                    self.booklist.remove(bookdict)
                    self.write_data()
                    self.borrowed_book.append(bookdict)
                    print("Book Borrowed")
                    return None
            print("Book not available in Library")
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))

    def return_book(self):
        try:
            enter_book = input("Enter book name To Return: ").lower()
            for bookdict in self.borrowed_book:
                if bookdict["book_name"].lower() == enter_book:
                    self.borrowed_book.remove(bookdict)
                    self.booklist.append(bookdict)
                    self.write_data()
                    print("Book Returned")
                    return None
            print("Book Cannot be Returned")
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))
