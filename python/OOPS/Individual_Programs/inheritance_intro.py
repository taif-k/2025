class Upi:
    def __init__(self):
        pass

    def payment_mode(self): 
        self.start_line = "We have"
        print(f"{self.start_line} Fast online payment")

    def small_transactions(self):
        print(f"{self.start_line} Upi lite option")

class Paytm(Upi):
    def __init__(self):
        pass
        
    def online_bank(self):
        print(f"{self.start_line} our own Bank")

    def refer(self):
        print(f"{self.start_line} Refer and earn feature")

class Phonepe(Paytm):
    def __init__(self):
        pass

    def wallet(self):
        print(f"{self.start_line} Wallet option")
    print("--Welcome to Phonepe--")

app = Phonepe()
app.payment_mode()
app.small_transactions()
app.wallet()
app.refer()

