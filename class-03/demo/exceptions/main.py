
# print("let's do something totally wrong. See if you can spot me in the output!")
# print("Too many parentheses"))

# print("More wrongness. Do I get printed?")
# print("Who has ever 'messed up' quotations marks?")

# print("What happens now? Do you see me printed?")
# value = 1/0

# try:
#     print('Divide by Zero again ', 1/0)
# except ZeroDivisionError:
#     print('Invalid Input')

# try:
#     print("Divide by zero again", 1 / "spam")
# except:
#     print("Don't divide by zero silly.")
#
# print("Total lie!. The problem was not dividing by zero. It was a type error")


# try:
#     spam = "nonsense" / 42
# except ZeroDivisionError:
#     print("Don't divide by zero silly.")
# except Exception as e:  # notice we can refer to the exception using 'as'
#     # print("So sorry end user. Something broke!")
#     print(e)

# try:
#     value = True + " nonsense"  # change to str(True) and see what happens
# except TypeError as e:
#     print(f"Something broke! Details: {e}")
# except ZeroDivisionError:
#     print('Dont Divide by 0')
# else:
#     print(f"smooth sailing. value is {value}")
# finally:
#     print("clean up mess as needed")

age = 20

if age < 21:
    raise ValueError("Invalid age - Gotta be at least 21 for this Party!")
    # or
    raise Exception("Invalid age - Gotta be at least 21 for this Party!")
