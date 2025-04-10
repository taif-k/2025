
def numbers_input():
        while True:
            first_number = input("Enter First Number: ")
            if first_number.isdigit():
                first_number = int(first_number)
                while True:
                    second_number = input("Enter Second Number: ")
                    if second_number.isdigit():
                        second_number = int(second_number)
                        break
                break 
        return first_number,second_number 