import inputnumbers

def divide():
    firstnum,secondnum = inputnumbers.numbers_input()
    if secondnum !=0:
        return firstnum / secondnum
    else:
        print("Second number should not be zero")
        # firstnum,secondnum = inputnumbers.numbers_input()
        try:
            data=firstnum / secondnum
        except:
            print("Number can not be devide by 0")
        return data
