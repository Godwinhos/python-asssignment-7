"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    pass

def deposit(account_number, amount):
    """Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
    """
    pass

def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    pass

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""
    pass

# Dictionary to store all accounts
accounts = {}

# Function to create account
def create_account(account_number, name, balance=0.0, **kwargs):
    accounts[account_number] = {
        "name": name,
        "balance": balance
    }
    # Add extra info (like overdraft_limit, account_type, etc.)
    for key, value in kwargs.items():
        accounts[account_number][key] = value
    print(f"Account {account_number} created for {name} with balance {balance}")

# Deposit money (supports batch deposits with *args)
def deposit(account_number, *amounts):
    if account_number in accounts:
        for amt in amounts:
            accounts[account_number]["balance"] += amt
            print(f"Deposited {amt} into {account_number}")
    else:
        print("Account not found!")

# Withdraw money (supports batch withdrawals with *args)
def withdraw(account_number, *amounts):
    if account_number in accounts:
        for amt in amounts:
            if accounts[account_number]["balance"] >= amt:
                accounts[account_number]["balance"] -= amt
                print(f"Withdrew {amt} from {account_number}")
            else:
                print("Insufficient funds!")
    else:
        print("Account not found!")

# Transfer money between accounts
def transfer(from_acc, to_acc, amount):
    if from_acc in accounts and to_acc in accounts:
        if accounts[from_acc]["balance"] >= amount:
            accounts[from_acc]["balance"] -= amount
            accounts[to_acc]["balance"] += amount
            print(f"Transferred {amount} from {from_acc} to {to_acc}")
        else:
            print("Insufficient funds for transfer!")
    else:
        print("One or both accounts not found!")

# Get account report
def account_report(account_number):
    if account_number in accounts:
        print(f"Report for {account_number}: {accounts[account_number]}")
    else:
        print("Account not found!")


# ---------------- DEMO ----------------
create_account("101", "Alice", 500, overdraft_limit=200)
create_account("102", "Bob", 300)

deposit("101", 100, 50, 25)      # multiple deposits
withdraw("102", 50, 30)          # multiple withdrawals
transfer("101", "102", 200)      # transfer

account_report("101")
account_report("102")

