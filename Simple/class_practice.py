class BankAccount:
    """
    A class to represent a bank account.
    """

    def __init__(self, holder_name, initial_balance=0):
        """
        Constructor to initialize the account holder's name and balance.

        Args:
            holder_name (str): Name of the account holder.
            initial_balance (float): Initial balance of the account (default is 0).
        """
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposits money into the account.

        Args:
            amount (float): Amount to deposit.

        Returns:
            None
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws money from the account if sufficient balance exists.

        Args:
            amount (float): Amount to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_balance(self):
        """
        Displays the current account balance.

        Returns:
            None
        """
        print(f"Account holder: {self.holder_name}, Balance: {self.balance}")


# Example usage
if __name__ == "__main__":
    # Create a bank account object
    account = BankAccount("John Doe", 100)
    
    # Display initial balance
    account.display_balance()  # Output: Account holder: John Doe, Balance: 100

    # Deposit money
    account.deposit(50)        # Output: Deposited 50. New balance: 150

    # Withdraw money
    account.withdraw(30)       # Output: Withdrew 30. New balance: 120
    account.withdraw(200)      # Output: Insufficient balance!

    # Display final balance
    account.display_balance()  # Output: Account holder: John Doe, Balance: 120