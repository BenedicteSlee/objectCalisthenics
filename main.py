class MinPlayers(object):
    number = 7


class MaxPlayers(object):
    number = 10


class Player(object):
    def __init__(self, gender):
        self.gender = gender


class Male(Player):
    def __init__(self):
        pass


class Female(Player):
    def __init__(self):
        pass


class Team(object):
    def __init__(self, players):
        if len(players) < MinPlayers.number:
            raise ValueError
        if len(players) > MaxPlayers.number:
            raise ValueError

        print len(players)
        print type(players[0])
        self.nFemale = sum([1 for x in players if isinstance(x, Female)])
        self.nMale = sum([1 for x in players if isinstance(x, Male)])

        if self.nFemale < 2 or self.nMale < 2:
            print self.nFemale
            print self.nMale
            raise ValueError

        self.players = players


