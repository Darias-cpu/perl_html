class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}.")

# Creating a bank account for a user
account = BankAccount("Alice", 100)

# Checking the balance
account.check_balance()  # Output: Current balance: $100.

# Depositing money
account.deposit(50)      # Output: Deposited: $50. New balance: $150.

# Withdrawing money
account.withdraw(30)     # Output: Withdrew: $30. New balance: $120.

# Attempting to withdraw more than the balance
account.withdraw(200)    # Output: Withdrawal amount must be positive and less than or equal to the balance.

# Checking the final balance
account.check_balance()   # Output: Current balance: $120.
