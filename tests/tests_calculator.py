import unittest 
from src.Calculator import *

class CalculatorTests(unittest.TestCase):
  def test_sum(self):
    assert sum(3,2) == 5

  def test_substract(self):
    assert substract(10,5) == 5
  
  def test_multiply(self):
    assert multiply(3,4) == 12

  def test_divide(self):
    self.assertEqual(divide(14,2), 7, "Division 14 / 2")
  
  def test_divide_by_zero(self):
      # Usando assertRaises como contexto
      with self.assertRaises(ValueError) as context:
          divide(10, 0)
    

