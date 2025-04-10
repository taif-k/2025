import inputnumbers

def addition():
    firstnum,secondnum = inputnumbers.numbers_input()
    add = firstnum + secondnum
    return add

def divide():
    try:
        firstnum,secondnum = inputnumbers.numbers_input()
        div = firstnum / secondnum
        return div
    except:
        print("Second number should not be Zero")
        return divide()

def subtraction():
    firstnum,secondnum = inputnumbers.numbers_input()
    sub = firstnum - secondnum
    return sub

def multiply():
    firstnum,secondnum = inputnumbers.numbers_input()
    mul = firstnum * secondnum
    return mul