import inputnumbers
import sys,os
sys.path.append(os.getcwd())
import python

err_log = r"D:\Repositories\2025\python\Programs\errordetails.txt"

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
        python.update_errorslog(python.error_details(e),err_log)
        return divide()

def subtraction():
    firstnum,secondnum = inputnumbers.numbers_input()
    sub = firstnum - secondnum
    return sub

def multiply():
    firstnum,secondnum = inputnumbers.numbers_input()
    mul = firstnum * secondnum
    return mul