"""
Bank Account System using Python OOP Concepts
Demonstrates: Classes, Objects, Inheritance, Encapsulation, and Polymorphism
"""
#import the date time class from Python,s built-in datetime module
from datetime import datetime
#import List from the typing module
from typing import List


# Parent Class (Base Class)
class BankAccount:
    """Base class for all bank accounts"""

    # Class variable (shared across all instances)
    total_accounts = 0

    def __init__(self, account_holder: str, initial_balance: float = 0):
        """
        Initialize a bank account

        Args:
            account_holder: Name of the account holder
            initial_balance: Initial deposit amount (default: 0)
        """
        # Instance variables (unique to each object)
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self._generate_account_number()
        self.transaction_history: List[str] = []

        # Add initial balance to history if not zero
        if initial_balance > 0:
            self.transaction_history.append(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Initial Deposit: ${initial_balance:.2f}"
            )

        # Increment total accounts
        BankAccount.total_accounts += 1

    def _generate_account_number(self) -> str:
        """Generate a unique account number"""
        return f"ACC{BankAccount.total_accounts + 1:05d}"

    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account

        Args:
            amount: Amount to deposit

        Returns:
            True if deposit successful, False otherwise
        """
        if amount <= 0:
            print("❌ Error: Deposit amount must be positive!")
            return False

        self.balance += amount
        transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deposit: +${amount:.2f}"
        self.transaction_history.append(transaction)
        print(f"✅ Successfully deposited ${amount:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account

        Args:
            amount: Amount to withdraw

        Returns:
            True if withdrawal successful, False otherwise
        """
        if amount <= 0:
            print("❌ Error: Withdrawal amount must be positive!")
            return False

        if amount > self.balance:
            print(f"❌ Error: Insufficient funds! Available balance: ${self.balance:.2f}")
            return False

        self.balance -= amount
        transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Withdrawal: -${amount:.2f}"
        self.transaction_history.append(transaction)
        print(f"✅ Successfully withdrew ${amount:.2f}")
        return True

    def get_balance(self) -> float:
        """Get current account balance"""
        return self.balance

    def display_account_info(self) -> None:
        """Display account information"""
        print("\n" + "=" * 50)
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.__class__.__name__}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("=" * 50)

    def display_transaction_history(self) -> None:
        """Display all transactions"""
        print("\n" + "=" * 50)
        print(f"Transaction History for {self.account_holder}")
        print("=" * 50)
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)
        print("=" * 50)

    def __str__(self) -> str:
        """String representation of the account"""
        return f"{self.account_holder} ({self.account_number}): ${self.balance:.2f}"

    def __repr__(self) -> str:
        """Developer-friendly representation"""
        return f"BankAccount('{self.account_holder}', {self.balance})"


# Child Class 1 - Inheritance Example
class SavingsAccount(BankAccount):
    """Savings account with interest and withdrawal limits"""

    def __init__(self, account_holder: str, initial_balance: float = 0, interest_rate: float = 0.03):
        """
        Initialize a savings account

        Args:
            account_holder: Name of the account holder
            initial_balance: Initial deposit amount
            interest_rate: Annual interest rate (default: 3%)
        """
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
        self.withdrawal_count = 0
        self.monthly_withdrawal_limit = 3

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw with limit (max 3 times per month)

        Args:
            amount: Amount to withdraw

        Returns:
            True if withdrawal successful, False otherwise
        """
        if self.withdrawal_count >= self.monthly_withdrawal_limit:
            print(f"❌ Error: Monthly withdrawal limit ({self.monthly_withdrawal_limit}) reached!")
            return False

        if super().withdraw(amount):
            self.withdrawal_count += 1
            return True
        return False

    def apply_interest(self) -> None:
        """Apply interest to the account"""
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Interest Applied: +${interest_amount:.2f}"
        self.transaction_history.append(transaction)
        print(f"✅ Interest applied: ${interest_amount:.2f}")

    def reset_monthly_limit(self) -> None:
        """Reset monthly withdrawal counter"""
        self.withdrawal_count = 0
        print("✅ Monthly withdrawal limit reset")

    def display_account_info(self) -> None:
        """Override: Display savings account info with interest rate"""
        super().display_account_info()
        print(f"Interest Rate: {self.interest_rate * 100:.2f}%")
        print(f"Withdrawals This Month: {self.withdrawal_count}/{self.monthly_withdrawal_limit}")


# Child Class 2 - Inheritance Example
class CheckingAccount(BankAccount):
    """Checking account with overdraft protection"""

    def __init__(self, account_holder: str, initial_balance: float = 0, overdraft_limit: float = 500):
        """
        Initialize a checking account

        Args:
            account_holder: Name of the account holder
            initial_balance: Initial deposit amount
            overdraft_limit: Maximum overdraft allowed (default: $500)
        """
        super().__init__(account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw with overdraft protection

        Args:
            amount: Amount to withdraw

        Returns:
            True if withdrawal successful, False otherwise
        """
        if amount <= 0:
            print("❌ Error: Withdrawal amount must be positive!")
            return False

        available_funds = self.balance + self.overdraft_limit

        if amount > available_funds:
            print(f"❌ Error: Cannot exceed available funds (${available_funds:.2f})")
            return False

        self.balance -= amount
        transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Withdrawal: -${amount:.2f}"
        self.transaction_history.append(transaction)

        if self.balance < 0:
            print(f"⚠️  Warning: You are in overdraft. Current balance: ${self.balance:.2f}")
        else:
            print(f"✅ Successfully withdrew ${amount:.2f}")
        return True

    def display_account_info(self) -> None:
        """Override: Display checking account info with overdraft limit"""
        super().display_account_info()
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")
        print(f"Available Funds (including overdraft): ${self.balance + self.overdraft_limit:.2f}")


# Demonstration
def main():
    """Demonstrate the bank account system"""

    print("\n" + "🏦 BANK ACCOUNT SYSTEM - OOP DEMONSTRATION 🏦".center(50))
    print("=" * 50)

    # Create different account objects
    print("\n--- Creating Accounts ---\n")

    # Savings Account
    savings = SavingsAccount("Alice Johnson", 5000, interest_rate=0.04)
    print(f"Created: {savings}")

    # Checking Account
    checking = CheckingAccount("Bob Smith", 2000, overdraft_limit=1000)
    print(f"Created: {checking}")

    # Regular Bank Account
    regular = BankAccount("Charlie Brown", 1000)
    print(f"Created: {regular}")

    # Display account information
    print("\n--- Account Information ---")
    savings.display_account_info()
    checking.display_account_info()

    # Perform transactions
    print("\n--- Performing Transactions ---\n")

    print("💰 SAVINGS ACCOUNT TRANSACTIONS:")
    savings.deposit(1000)
    savings.withdraw(500)
    savings.apply_interest()

    print("\n💰 CHECKING ACCOUNT TRANSACTIONS:")
    checking.deposit(500)
    checking.withdraw(2500)  # This will use overdraft
    checking.withdraw(1500)  # This will use more overdraft

    print("\n💰 REGULAR ACCOUNT TRANSACTIONS:")
    regular.deposit(2000)
    regular.withdraw(1500)

    # Display final balances
    print("\n--- Final Account Status ---")
    print(f"\nTotal accounts created: {BankAccount.total_accounts}")
    print(f"\nSavings Account: {savings}")
    print(f"Checking Account: {checking}")
    print(f"Regular Account: {regular}")

    # Display transaction histories
    savings.display_transaction_history()
    checking.display_transaction_history()


if __name__ == "__main__":
    main()

