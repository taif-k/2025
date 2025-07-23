import sys,os
sys.path.append(os.getcwd())
from python.OOPS.Library_Management_System.src.Domain.option_menu import BookMenu
bookdata = r"D:\Repositories\2025\python\OOPS\Library_Management_System\src\Database\bookdata.json"

book_obj = BookMenu(bookdata)
book_obj.menu_option()