import sys,os
# print(sys.path)
sys.path.append(os.getcwd())
from python.Utils.file_io import file_io_obj

class BankAccout:
    def __init__(self):
        self.__account_no = 1234567890
        self.__totalbalance = 500
        self.__pin = 123

    def task_option(self):
        print("1-withdraw")
        print("2-Deposit")
        print("3-check balance")

    def verifyaccount(self):
        try:
            enter_accountno = int(input("Enter account no: "))
            if enter_accountno == self.__account_no:
                enter_pin = int(input("Enter pin to verify: "))
                if enter_pin == self.__pin:
                    while True:
                        self.task_option()
                        ask_option = int(input("Enter option: "))
                        if ask_option == 1:
                            self.withdrawl()
                        elif ask_option == 2:
                            self.deposit()
                        elif ask_option == 3:
                            balance = self.__totalbalance
                            print(f"Total balance is {balance}")
                        else:
                            break
                else:
                    print("Incorrect pin")
            else:
                print("Enter valif account number to proceed further") 
        except Exception as e:
            print("checking error log")
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))                       

    def withdrawl(self):
        self.withdraw_amount = int(input("Enter amount to withdrawl: "))
        if self.withdraw_amount <= self.__totalbalance: 
            self.__totalbalance -= self.withdraw_amount
        else:
            print("Withdraw amount greater than total balance")

    def deposit(self):
        self.deposit_amount = int(input("Enter amount to deposit: "))
        if self.deposit_amount >= 0:   
            self.__totalbalance += self.deposit_amount
        else:
            print("Enter valid amount")

if __name__ == "__main__":
    try:
        account1 = BankAccout()
        account1.verifyaccount()
    except BaseException as e:
        print("\nBase Exception error logged in error file")
        file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))