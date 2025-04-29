# over loading is compile time polymorphism

class Main:
    def one(self,param1,param2):
        print("This is main one")

    def one(self,param1,param2,param3=0):
        print(param1,param2,param3)
        print("this is 2nd main one")

class Sub(Main):
    def one(self,param1,param2,param3=0):
        print()
        print(param1,param2,param3)
        print("This is sub one")

object = Main()
object.one("nine","eight")

object2 = Sub()
object2.one(9,8,7)


