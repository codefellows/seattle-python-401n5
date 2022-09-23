"""Place in root of Project,
at same level as pyproject.toml
"""

from abc import ABC, abstractmethod
import builtins
import re
from ten_thousand.game import Game
from ten_thousand.game_logic import GameLogic
from collections import Counter


class BaseBot(ABC):
    """Base class for Game bots"""

    def __init__(self, print_all=False):
        self.last_print = ""
        self.last_roll = []
        self.print_all = print_all
        self.dice_remaining = 0
        self.unbanked_points = 0

        self.real_print = print
        self.real_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        """restores the real print and input builtin functions"""

        builtins.print = self.real_print
        builtins.input = self.real_input

    def report(self, text):
        """Prints out final score, and all other lines optionally"""

        if self.print_all:
            self.real_print(text)
        elif text.startswith("Thanks for playing."):
            score = re.sub("\D", "", text)
            self.total_score += int(score)

    def _mock_print(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        line = " ".join(args)

        if "unbanked points" in line:

            # parse the proper string
            # E.g. "You have 700 unbanked points and 2 dice remaining"
            unbanked_points_part, dice_remaining_part = line.split("unbanked points")

            # Hold on to unbanked points and dice remaining for determining rolling vs. banking
            self.unbanked_points = int(re.sub("\D", "", unbanked_points_part))

            self.dice_remaining = int(re.sub("\D", "", dice_remaining_part))

        elif line.startswith("*** "):

            self.last_roll = [int(ch) for ch in line if ch.isdigit()]

        else:
            self.last_print = line

        self.report(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        if self.last_print == "(y)es to play or (n)o to decline":

            return "y"

        elif self.last_print == "Enter dice to keep, or (q)uit:":

            return self._enter_dice()

        elif self.last_print == "(r)oll again, (b)ank your points or (q)uit:":

            return self._roll_bank_or_quit()

        raise ValueError(f"Unrecognized last print {self.last_print}")

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        roll_string = ""

        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)

        return roll_string

    @abstractmethod
    def _roll_bank_or_quit(self):
        """decide whether to roll the dice, bank the points, or quit"""

        # subclass MUST implement this method
        pass

    @classmethod
    def play(cls, num_games=1):
        """Tell Bot play game a given number of times.
        Will report average score"""

        mega_total = 0

        for _ in range(num_games):
            player = cls()
            game = Game()
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"{cls.__name__}: {num_games} games played with average score of {mega_total // num_games}"
        )


class NervousNellie(BaseBot):
    """NervousNellie banks the first roll always"""

    def _roll_bank_or_quit(self):
        return "b"


class MiddlingMargaret(BaseBot):
    """MiddlingMargaret has a moderate playing style"""

    def _roll_bank_or_quit(self):

        if self.unbanked_points >= 500 or self.dice_remaining < 3:
            return "b"

        return "r"


class DaringDarla(BaseBot):
    """DaringDarla rolls whenever more than 1 dice remaining """

    def _roll_bank_or_quit(self):
        if self.dice_remaining == 1:
            return "b"

        return "r"


class YourBot(BaseBot):
    def _roll_bank_or_quit(self):
        """your logic here"""
        return "b"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        return super()._enter_dice()


class MarkBot(BaseBot):
    """
    self.dice_remaining
    self.unbanked_points
    self.total_score
    """

    def __init__(self):
        from collections import Counter

        self.Counter = Counter
        super().__init__()
        self.rounds_remaining = None

    # this is a pretty close approximation of chance to fail, could be improved
    @staticmethod
    def chance_to_fail(num_of_dice):
        return {
            1: 2 / 3,
            2: 4 / 9,
            3: 8 / 27 - 1 / 36,
            4: 16 / 81 - 1 / 36,
            5: 32 / 243 - 1 / 36,
            6: 64 / 729 - 1 / 36 - 1 / 6 ** 6,
        }[num_of_dice]

    def _roll_bank_or_quit(self):
        # always roll when you have 6 dice to roll
        if not self.dice_remaining or self.dice_remaining == 6:
            return "r"
        # bank if we think we have a high chance of failure
        if MarkBot.chance_to_fail(self.dice_remaining) > 95 / (
            self.unbanked_points + 1
        ):
            return "b"
        return "r"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        # if we all dice score, please keep them all
        # if we are intending on banking, lets keep all scoring dice
        if len(roll) == len(self.last_roll) or self._roll_bank_or_quit() == "b":
            # self.real_print("\nINTENDING TO BANK:",self.dice_remaining)
            for value in roll:
                roll_string += str(value)
            self.report("> " + roll_string)
            return roll_string
        # lets go for highest average of points per die
        highest_score_per_die = 0
        highest_scoring_dice = 0
        highest_scoring_len = 0
        # check each combination of dice, to determine the 'best' value per die, and keep that set
        roll = list(roll)
        roll.sort()
        for i in range(len(roll)):
            for j in range(len(roll)):
                if len(roll[i : j + 1]):
                    test_dice = roll[i : j + 1]
                    test_score = GameLogic.calculate_score(roll[i : j + 1]) / len(
                        test_dice
                    )
                    if test_score > highest_score_per_die:
                        highest_score_per_die = test_score
                        highest_scoring_dice = test_dice
                        highest_scoring_len = len(test_dice)
                    elif test_score == highest_score_per_die:
                        if highest_score_per_die >= 175:
                            if len(test_dice) > highest_scoring_len:
                                highest_score_per_die = test_score
                                highest_scoring_dice = test_dice
                                highest_scoring_len = len(test_dice)
        for value in highest_scoring_dice:
            roll_string += str(value)
        self.report("> " + roll_string)
        return roll_string


class YoniBot(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 550 or self.dice_remaining < 2:
            return "b"
        if self.unbanked_points >= 450 and self.dice_remaining <= 3:
            return "b"
        elif self.unbanked_points >= 350 and self.dice_remaining == 2:
            return "b"
        if self.unbanked_points + self.total_score >= 10000:
            return "b"
        return "r"


class GamblingBotThree(BaseBot):
    """
    self.dice_remaining
    self.unbanked_points
    self.total_score
    """
    def __init__(self):
        from collections import Counter
        self.Counter = Counter
        super().__init__()
        self.rounds_remaining = None
    # this is a pretty close approximation of chance to fail, could be improved
    @staticmethod
    def chance_to_fail(num_of_dice):
        return {
            1: 2 / 3,
            2: 4 / 9,
            3: 8 / 27 - 1 / 36,
            4: 16 / 81 - 1 / 36,
            5: 32 / 243 - 1 / 36,
            6: 64 / 729 - 1 / 36 - 1 / 6 ** 6,
        }[num_of_dice]
    def _roll_bank_or_quit(self):
        # always roll when you have 6 dice to roll
        if self.unbanked_points >= 3000 or self.dice_remaining == 6:
            return "b"
        if not self.dice_remaining or self.dice_remaining == 5:
            return "r"
        roll_tuple = GameLogic.get_scorers(self.last_roll)
        roll = list(roll_tuple)
        abcs = [0, 0, 0, 0, 0, 0]
        # This is the array of how many times the integers 1-6 are represented
        for number in roll:
            abcs[number-1] += 1
            # This is counting how many of each number we have in our array. Number -1 is because our numbers 1-6 are reindexed to 0-5 to to into a list. The location in the array (0-5) are getting added a number of the count.
        if abcs[3] >=3 or abcs[4] >=3 or abcs[5]>=3:
            return "b"
            #If there are triples or more in 4,5,6 bank it
        if GamblingBotThree.chance_to_fail(self.dice_remaining) > 100 / (self.unbanked_points + 1):
            return "b"
        if self.unbanked_points >= 550 or self.dice_remaining < 3:
            return "b"
        if self.unbanked_points >= 450 and self.dice_remaining < 2:
            return "b"
        elif self.unbanked_points >= 350 and self.dice_remaining == 1:
            return "b"
        if self.unbanked_points + self.total_score >= 10000:
            return "b"
        return "r"
    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        # if we all dice score, please keep them all
        # if we are intending on banking, lets keep all scoring dice
        if len(roll) == len(self.last_roll) or self._roll_bank_or_quit() == "b":
            # self.real_print("\nINTENDING TO BANK:",self.dice_remaining)
            for value in roll:
                roll_string += str(value)
            self.report("> " + roll_string)
            return roll_string
        # lets go for highest average of points per die
        highest_score_per_die = 0
        highest_scoring_dice = 0
        highest_scoring_len = 0
        # check each combination of dice, to determine the 'best' value per die, and keep that set
        roll = list(roll)
        roll.sort()
        for i in range(len(roll)):
            for j in range(len(roll)):
                if len(roll[i : j + 1]):
                    test_dice = roll[i : j + 1]
                    #This is finding out if you have a one essentially as it is looking for one die
                    test_score = GameLogic.calculate_score(roll[i : j + 1]) / len(
                        test_dice
                    )
                    #This is just checking your different combinations of die
                    if test_score > highest_score_per_die:
                        highest_score_per_die = test_score
                        highest_scoring_dice = test_dice
                        highest_scoring_len = len(test_dice)
                    elif test_score == highest_score_per_die:
                        if highest_score_per_die >= 500:
                            if len(test_dice) > highest_scoring_len:
                                highest_score_per_die = test_score
                                highest_scoring_dice = test_dice
                                highest_scoring_len = len(test_dice)
        for value in highest_scoring_dice:
            roll_string += str(value)
        listy_list = [number for number in roll_string]
        if listy_list.count(5)==2 and listy_list.count(1)==0:
            roll_string = ""
            listy_list.remove(5)
            roll_string = "".join(listy_list)
            roll_string += "5"
        self.report("> " + roll_string)
        return roll_string


class Frogs(BaseBot):
    def _roll_bank_or_quit(self):
        combinations = (
            {'dice_left': 1, 'min_points': 400},
            {'dice_left': 2, 'min_points': 550},
            {'dice_left': 3, 'min_points': 650},
            {'dice_left': 4, 'min_points': 900},
            {'dice_left': 4, 'min_points': 1800}
        )

        for combination in combinations:
            if self.dice_remaining == combination['dice_left'] and self.unbanked_points > combination['min_points']:
                return "b"
        return "r"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        if len(roll) == len(self.last_roll):
            return self._process_roll(roll)

        if Counter(roll)[1] and Counter(roll)[5] < 3:
            roll = tuple(dice for dice in roll if dice != 5)

        if Counter(roll)[5] == 2:
            new_roll = [*roll]
            new_roll.remove(5)
            roll = tuple(new_roll)

        if Counter(roll)[1] == 2:
            new_roll = [*roll]
            new_roll.remove(1)
            roll = tuple(new_roll)

        if len(Counter(roll)) > 1:
            new_roll = [dice for dice in roll if dice != 2]
            roll = tuple(new_roll)

        if len(Counter(roll)) > 1 and Counter(roll)[3] < 4:
            new_roll = [dice for dice in roll if dice != 3]
            return self._process_roll(tuple(new_roll))

        return self._process_roll(roll)

    def _process_roll(self, roll):

        roll_string = ""

        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)

        return roll_string


class Botmius_prime(BaseBot):
    def _roll_bank_or_quit(self):
        """your logic here"""
        if self.dice_remaining > 300:
            return 'r'
        return 'b'
    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        dice_index = []
        # checks for 1's and 5's
        def dice_check(list):
            # if 1 then check for 5's as well
            if 1 in self.last_roll:
                # if 5's then add both ones and 5's to list
                if 5 in self.last_roll:
                    for index in range(len(self.last_roll)):
                        if self.last_roll[index] == 1:
                            list.append(index)
                        if self.last_roll[index] == 5:
                            list.append(index)
                else:
                    # only add 1's if no 5's in list
                    for index in range(len(self.last_roll)):
                        if self.last_roll[index] == 1:
                            list.append(index)
            # if 5's in list by itself, append only the 5's location
            elif 5 in self.last_roll:
                for index in range(len(self.last_roll)):
                    if self.last_roll[index] == 5:
                        list.append(index)
            return str(list)
        return super()._enter_dice()

    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 1500:
            return "b"
        return "r"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        if len(roll) >= len(self.last_roll):
            return self._process_roll(roll)

        return self._process_roll(tuple())

    def _process_roll(self, roll):

        roll_string = ""

        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)

        return roll_string


class Frogs2(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 1500:
            return "b"
        return "r"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        if len(roll) >= len(self.last_roll):
            return self._process_roll(roll)

        return self._process_roll(tuple())

    def _process_roll(self, roll):

        roll_string = ""

        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)

        return roll_string


if __name__ == "__main__":
    num_games = 1
    for _ in range(10000):
    # NervousNellie.play(num_games)
    # GamblingBotThree.play(num_games)
        Frogs2.play(num_games)
    # Botmius_prime.play(num_games)
    # MiddlingMargaret.play(num_games)
    # DaringDarla.play(num_games)
    # MarkBot.play(num_games)
    # YourBot.play(num_games)
