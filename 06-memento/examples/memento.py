import copy

from pprint import pprint as pp


def Memento(obj, deep=False):
    state = (copy.copy, copy.deepcopy)[bool(deep)](obj.__dict__)
    def Restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)
    return Restore


class Transaction:
    """A transaction guard. This is realy just
    syntactic suggar arount a memento closure.
    """
    deep = False
    def __init__(self, *targets):
        self.targets = targets
        self.Commit()
    def Commit(self):
        self.states = [Memento(target, self.deep) for target in self.targets]

    def Rollback(self):
        for state in self.states:
            state()


class GamePlayer:
    health_points = 100

    def drink_potion(self):
        self.health_points += 10

    def take_damage(self):
        self.health_points -= 20

    def power_goes_out(self):
        self.health_points = self.health_points/0


if __name__ == '__main__':
    zelda = GamePlayer()
    t = Transaction(zelda)

    # import pdb; pdb.set_trace()

    try:

        print('Zelda is about to go through the Marshlands')
        zelda.take_damage()
        zelda.take_damage()
        zelda.take_damage()
        zelda.drink_potion()

        t.Commit()
        print('Zelda goes through the Marshlands')
    except:
        t.Rollback()
        pass

    print('Zelda looks like: ')
    pp(zelda.__dict__)

    try:
        print('Zelda going through the Dungeon')
        zelda.drink_potion()
        zelda.drink_potion()
        zelda.power_goes_out()

        t.Commit()
        print('Zelda goes through the dungeon')
    except:
        t.Rollback()
        pass

    print('Zelda looks like: ')
    pp(zelda.__dict__)


