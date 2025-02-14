# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
  number = numbers[-1] + 1
  
  if len(numbers) % 5 != 0:
    numbers.append(number)
    add_numbers_to_list(numbers)

if __name__ == "__main__":
  numbers = [1,3,4,5,10,11]
  add_numbers_to_list(numbers)
  print(numbers)