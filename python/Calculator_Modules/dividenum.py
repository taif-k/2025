import inputnumbers

def divide():
    firstnum,secondnum = inputnumbers.numbers_input()
    if secondnum !=0:
        return firstnum / secondnum
    else:
        print("Second number should not be zero")
        firstnum,secondnum = inputnumbers.numbers_input()
        return firstnum / secondnum
