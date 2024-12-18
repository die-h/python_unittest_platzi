import unittest
from src.BankAccount import *

class BankAccountTests(unittest.TestCase):
  def setUp(self) -> None:
    self.account = BankAccount(balance=1000)
  
  def test_deposit(self):
    new_balance = self.account.deposit(500)
    assert new_balance == 1500

  def test_withdraw(self):
    account = BankAccount(balance=1000)
    new_balance = self.account.withdraw(200)
    assert new_balance == 800

  def test_get_balance(self):
    balance = self.account.get_balance()
    assert balance == 1000
