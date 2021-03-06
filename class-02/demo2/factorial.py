def factorial(n):
    """
    return n! (as it's sometimes written)
    e.g. factorial(3) = 3 * 2 * 1 = 6

    Note: Normally wouldn't name a package or module this way
    but wanted to be really clear about which was which

    Bonus: hover your mouse over the function name when importing
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)

# factorial(4)
# 4 * factorial(3) -> 24
#   3 * factorial(2) -> 6
#       2 * factorial(1) ->2
#           return 1
