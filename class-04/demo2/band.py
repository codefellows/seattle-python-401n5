class Musician:

    def __init__(self, color):
        self.color = color
        # self.name = name
        # self.instrument = instrument

    def __str__(self):
        return f'{self.name} is jamin on his {self.color} {self.instrument}'


class Guitarist(Musician):
    def __init__(self, name, instrument, color):
        super().__init__(color)
        self.name = name
        self.instrument = instrument


if __name__ == '__main__':
    player1 = Guitarist('Roger', 'guitar', 'red')
    print(player1)
