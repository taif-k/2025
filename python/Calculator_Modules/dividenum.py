import inputnumbers

def divide():
    while True:
        firstnum,secondnum = inputnumbers.numbers_input()
        if secondnum !=0:
            div = firstnum / secondnum
            return div
        else:
            print("Second number should not be zero")
            

