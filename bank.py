class Amount:
    def __init__(self, amount: float, timestamp: str, transaction_type: str):
        self.amount = amount    
        self.timestamp = timestamp
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Transaction: {self.transaction_type}\nAmount: {self.amount}\nDate: {self.timestamp.split(' ')[0]}\nTime: {self.timestamp.split(' ')[1]}"


class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str, balance: float=0.0, transactions: list[Amount]=[]):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.transactions = transactions

    def deposit(self, amount: float):
        from datetime import datetime
        transaction = Amount(amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "DEPOSIT")
        self.__balance += amount
        self.transactions.append(transaction)

    def withdraw(self, amount: float):
        if self.__balance - amount < 0:
            print("Insufficient funds.")
        else:
            from datetime import datetime
            transaction = Amount(amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "WITHDRAWAL")
            self.__balance -= amount
            self.transactions.append(transaction)
            
    def print_transaction_history(self):
        if not self.transactions:
            print("You don't have any transactions.")

        else:
            for transaction in self.transactions:
                if isinstance(transaction, Amount):
                    print("---" * 10)
                    print(str(transaction))

    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
    def set_account_number(self, account_number: int):
        self.__account_number = account_number

    def get_account_holder(self):
        return self.__account_holder
    
    def set_account_holder(self, account_holder: str):
        self.__account_holder = account_holder

    def __str__(self):
        return f"Account number: {self.__account_number}\nAccount holder: {self.__account_holder}\nBalance: {self.__balance}"
    
    def __add__(self, amount: Amount):
        self.__balance += amount.get_balance()

    def __sub__(self, amount: Amount):
        if self.__balance - amount.get_balance() < 0:
            print("Insufficient funds.")
        else:
            self.__balance -= amount.get_balance()