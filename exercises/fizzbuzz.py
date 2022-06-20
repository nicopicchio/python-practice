# Requirements
# Write a function that accepts 2 numbers, lower and upper.

# The function should return an array containing all the numbers from lower to upper, including lower and upper themselves - with the following exceptions:

# Where a number is a multiple of three (3, 6, 9, etc.) the array should contain the string Fizz instead of the number.
# Where a number is a multiple of five (5, 10, etc.) the array should contain Buzz instead of of the number.
# For numbers which are multiples of both three and five (15, 30, etc.) the array should contain the string FizzBuzz instead of the number.

def fizzbuzz(lower, upper):
  range_array = list(range(lower, upper+1))
  for n in range_array:
    if n % 3 == 0 and n % 5 == 0:
      print('FizzBuzz')
    elif n % 3 == 0:
      print('Fizz')
    elif n % 5 == 0:
      print('Buzz')
    else:
      print(n)

fizzbuzz(1, 30)