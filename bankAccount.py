class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = .01, balance = 121): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self


# Create a BankAccount class with the attributes interest rate and balance

# Add a deposit method to the BankAccount class

# Add a withdraw method to the BankAccount class

# Add a display_account_info method to the BankAccount class

# Add a yield_interest method to the BankAccount class

# Create 2 accounts

accountOne = BankAccount()
accountTwo = BankAccount(.02, 640)

accountOne.deposit(40).deposit(40).deposit(100).withdraw(80).yield_interest().display_account_info()
accountTwo.deposit(200).deposit(200).withdraw(100).withdraw(100).withdraw(40).withdraw(20).yield_interest().display_account_info()

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
