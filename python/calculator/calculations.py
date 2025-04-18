import inputnumbers
import sys,os
sys.path.append(os.getcwd())
from python.Programs import get_currentdate,create_log

def addition():
    firstnum,secondnum = inputnumbers.numbers_input()
    add = firstnum + secondnum
    return add

def divide():
    try:
        firstnum,secondnum = inputnumbers.numbers_input()
        div = firstnum / secondnum
        return div
    except Exception as e:
        print("Second number should not be Zero")
        date = get_currentdate()
        errordetails = str({"mod":"calculations.py","func":"divide()","error":e,"date":date})
        create_log(errordetails)
        return divide()

def subtraction():
    firstnum,secondnum = inputnumbers.numbers_input()
    sub = firstnum - secondnum
    return sub

def multiply():
    firstnum,secondnum = inputnumbers.numbers_input()
    mul = firstnum * secondnum
    return mul