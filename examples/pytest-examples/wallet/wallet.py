class Wallet:

    def __init__(self, initial_amount=0):
        self.balance = initial_amount


    def add_cash(self, amount):
        self.balance += amount

        
    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not Enough Balance')
        
        self.balance -= amount


    
class InsufficientAmount(Exception):
    pass
