# This the banker class for 10,000
from random import randint
class Banker:
    """Banker class is responsible for tracking points 'on the shelf' and 'in the bank'"""

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def shelf(self, amt):
        self.shelved += amt

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def clear_shelved(self):
        self.shelved = 0


# Roll dice

@staticmethod
def roll_dice(num=6):
    return tuple([randint(1, 6) for _ in range(num)])


# End Game

if __name__ == '__main__':

    import sys

    def end_game():
        # print(f'Thanks for playing. You earned 0 points')
        sys.exit(f'Thanks for playing. You earned 0 points')
    end_game()
