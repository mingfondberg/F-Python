class BankAccount:
    def __init__(self, account_holder, balance=0):
        """
        Initierar en BankAccount-instans med kontoinnehavarens namn och initial balans.
        
        :param account_holder: Kontoinnehavarens namn
        :param balance: Initial balans (standard är 0)
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Sätter in ett belopp på kontot.
        
        :param amount: Beloppet som ska sättas in (måste vara ett positivt tal)
        """
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Tar ut ett belopp från kontot om det finns tillräckligt med medel.
        
        :param amount: Beloppet som ska tas ut (måste vara ett positivt tal)
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError("Balance too low.")
        else:
            raise ValueError("Withdrawal amount must be positive.")
    
    def get_balance(self):
        """
        Returnerar den aktuella balansen på kontot.
        """
        return self.balance
    
    def print_summary(self):
        """
        Skriver ut en sammanfattning av kontoinformationen.
        """
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

    def __repr__(self):
        return f"BankAccount(account_holder={self.account_holder!r}, balance={self.balance})"
