
class factorial:

    def __init__(self):
        self.inputnumber()

    def inputnumber(self):
        ask_number = int(input("Enter number to get its factorial: "))
        num = ask_number
        for n in range(ask_number-1,1,-1):
            ask_number *= n
        print(f"Factorial of {num} is: ",ask_number)

factorial_obj = factorial()