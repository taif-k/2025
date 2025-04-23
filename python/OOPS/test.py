class number:
    def __init__(self):
        print("hello")

    num = 3    

data = number()
print(data.num)




class details:

    def __init__(self,ID,NAME):
        print(f"ID: {ID} and name: {NAME}")
    # print("hi")

# details1 = details(101,"test")

# first, class variables are printed thn object's  

# printing order will be:
# 3
# hello
# 3
# hi
# ID: 101 and name: test  


