## Simple bank account 
Written on Python

### Navigation
- [Classes source code](bank.py)<br>
- [Testing file](main.py)<br>
- [UML diagram](UML_diagram.png)<br>

### bank.py
Contains 2 classes: Amount and PersonalAccount.

#### Amount class
**Attributes**
- amount: float
- timestamp: str (Used string instead of datetime.datetime)
- transaction_type: str

A class only has 1 method, the magic one: __str__()

#### PersonalAccount class
**Attributes**
- account_number: int
- account_holder: str 
- balance: float
- transactions: list

**Methods**
- deposit() -> None
- withdraw() -> None
- print_transaction_history() -> None
- get_balance() -> float
- get_account_number -> int
- set_account_number -> None
- get_account_holder -> str
- set_account_holder -> None

And some magic methods