class PersonalAccount:
    def __init__(self, account_number, account_holder, balance=0.0, transactions=[]):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.transactions = transactions

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