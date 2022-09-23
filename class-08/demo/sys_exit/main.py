import sys


def get_user_input():
    user_answer = input('Please Enter YOur Name')


def quit_game(message='Have a good Day!'):
    sys.exit(message)


if __name__ == '__main__':
    try:
        get_user_input()
        quit_game()
    except KeyboardInterrupt:
        quit_game('You have pressed CTRL-C')
