# fizz buzz
# Create a function that takes a number and returns somehting (string) or (int)
# if a number is div by 3, return fizz
# if a number is div by 5, return buzz
# if a number is div by 3 and 5, return fizzbuzz

# demo
#   fizz_buzz
#       - fizzbuzz.py
#       -__init__.py
#   tests
#       - test_fizzbuzz.py
#       -__init__.py

def fizz_buzz_function1(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


def fizz_buzz_function(num):
    word = ''
    if num % 3 == 0:
        word = 'Fizz'
    if num % 5 == 0:
        word += 'Buzz'

    return word or num
