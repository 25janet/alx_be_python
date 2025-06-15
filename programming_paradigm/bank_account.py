class BankAccount:
    """
    A class to represent a simple bank account.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The starting balance for the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self._account_balance = initial_balance  # Using a protected attribute for encapsulation

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self._account_balance += amount
        print(f"Deposited ${amount:.2f}.")
        self.display_balance()

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.

        Raises:
            ValueError: If the withdrawal amount is not positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")

        if self._account_balance >= amount:
            self._account_balance -= amount
            print(f"Withdrew ${amount:.2f}.")
            self.display_balance()
            return True
        else:
            print("Insufficient funds.")
            self.display_balance()
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Account Balance: ${self._account_balance:.2f}")