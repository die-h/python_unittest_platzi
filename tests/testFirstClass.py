def calculate_total(products : list[dict[str:str|float]]) -> float:
  total = 0
  for product in products:
    total += product["price"]
  return total


def test_calculate_total_with_empty_list():
  assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
  single : list[dict[str:str|float]] =[
  {
    "name": "pen", "price": 5
  }
  ]
  assert calculate_total(single) == 5

def test_calculate_total_with_multiple_products():

  multiple : list[dict[str:str|float]] =[
  {
    "name": "pen", "price": 5
  },
  {
    "name": "book", "price": 10
  }
  ]

  assert calculate_total(multiple) == 15

if __name__ == "__main__":
  test_calculate_total_with_empty_list()
  test_calculate_total_with_single_product()
  test_calculate_total_with_multiple_products()

