class ForceUser:

    # def __init__(self, force_power):
    #     self.force_power = force_power

    def attacking(self):
        return f'{self.name} is Force attacking!'

    def getting_hit(self):
        return f'{self.name} is being attacked!'

    @classmethod
    def get_count(cls):
        return JediMaster.count + SithLord.count


class JediMaster(ForceUser):

    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name='Random Master'):
        # super().__init__(force_power)
        self.name = name
        JediMaster.count += 1

    def __str__(self):
        return f'{self.name} is in the HOUSE!'

    def __repr__(self):
        return 'JediMaster("name")'

    @staticmethod
    def get_code():
        return 'There is no emotion, there is PEACE.'


class SithLord(ForceUser):

    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name='Random Sith'):
        self.name = name
        SithLord.count += 1

    @staticmethod
    def get_code():
        return 'Peace is a lie, there is only PASSION.'


if __name__ == '__main__':
    pass
    jedi1 = JediMaster('Old Ben')
    # jedi2 = JediMaster('Yoda')
    # jedi3 = JediMaster('Mace')
    # print(jedi1.name, jedi2.name, jedi3.name)
    print(jedi1.__repr__())
    # print(jedi1.force_power)
    # print(jedi2.attacking())
    # print(jedi3.attacking())

