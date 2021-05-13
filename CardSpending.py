class CreditCard:
    def __init__(self, customer, bank, acnt, limit, start_bal=0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = start_bal #R-2.7. - Q3

    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        if amount >= 0:
            self._balance -= amount
        else:
            raise ValueError('can not pay negative amount') #R-2.6. - Q2
if __name__ == '__main__':
    card1 = CreditCard('Becky Brown', 'Chase', '1234 5678', 3000)
    card2 = CreditCard('Greg Stanely', 'Farmers', '8765 4321', 2500, 250)
    print("Customer: ", card1._customer," // Bank: ", card1._bank," // Account Number: ", card1._account," // Limit: ", card1._limit," // Balance: ", card1._balance)
    print("Customer: ", card2._customer," // Bank: ", card2._bank," // Account Number: ", card2._account," // Limit: ", card2._limit," // Balance: ", card2._balance)
    print()
    print(card1._customer, " started with a balance of ", card1._balance," and made a payment of 50")
    card1.make_payment(50)
    print("New Card Balance is ", card1._balance)
    print()
    print(card2._customer, " started with a balance of ", card2._balance," and made a payment of 50")
    card2.make_payment(50)
    print("New Card Balance is ", card2._balance)
    print()


