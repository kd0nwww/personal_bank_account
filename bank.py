class Amount:
    def __init__(self, amount, timestamp, transaction_type):
        self.amount = amount
        self.timestamp = timestamp
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Transaction: {self.transaction_type}\nAmount: {self.amount}\nProccessed at: {self.timestamp}"
    
class PersonalAccount:
    def __init__(self, account_number, account_holder, balance=0.0, transactions=[]):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.transactions = transactions

    def print_transaction_history(self):
        if not self.transactions:
            print("You don't have any transactions.")
        else:
            for transaction in self.transactions:
                if isinstance(transaction, Amount):
                    print("---" * 10)
                    print(f"Transaction type: {transaction.transaction_type}")
                    print(f"Amount: {transaction.amount}")
                    print(f"Date: {transaction.timestamp}")

    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_holder(self):
        return self.__account_holder
    
    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder