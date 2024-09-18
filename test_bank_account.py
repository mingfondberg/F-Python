import pytest
from bank_module import BankAccount

def test_deposit():
    account = BankAccount("Alice", 100)
    account.deposit(50)
    assert account.get_balance() == 150

def test_withdraw():
    account = BankAccount("Bob", 200)
    account.withdraw(75)
    assert account.get_balance() == 125

def test_withdraw_too_much():
    account = BankAccount("Carol", 100)
    with pytest.raises(ValueError, match="Balance too low."):
        account.withdraw(150)

def test_negative_deposit():
    account = BankAccount("Dave", 50)
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account.deposit(-20)

def test_negative_withdraw():
    account = BankAccount("Eve", 75)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive."):
        account.withdraw(-10)
