import random


class Player:
    def __init__(self, name="default"):
        self.score = 0
        self.name = name
        self.winCount = 0

    def banks(self, pool, roundNum, rollNum):
        pass

    def add(self, pool):
        self.score += pool

    def reset(self):
        self.score = 0

    def won(self):
        self.winCount += 1

    def __str__(self):
        return f"{self.name} - {self.score}"


class UserPlayer(Player):
    def banks(self, pool, roundNum, rollNum):
        output = input(f"Bank? Pool: {pool}, Round: {roundNum} (Y/N): ")

        if output.lower() == "y":
            return True
        else:
            return False


class FiveHundredPlayer(Player):
    def banks(self, pool, roundNum, rollNum):
        if pool > 500:
            return True
        return False


class TwoHundredPlayer(Player):
    def banks(self, pool, roundNum, rollNum):
        if pool > 200:
            return True
        return False


class HundredPlayer(Player):
    def banks(self, pool, roundNum, rollNum):
        if pool > 100:
            return True
        return False


class OneSevenFivePlayer(Player):
    def banks(self, pool, roundNum, rollNum):
        if pool > 175:
            return True
        return False


class OneFiftyPlayer(Player):
    def banks(self, pool, roundNum, rollNum):
        if pool > 150:
            return True
        return False


class SixFiftyPlayer(Player):
    def banks(self, pool, roundNum, rollNum):
        if pool > 650:
            return True
        return False


class MainPlayer(Player):
    def banks(self, pool, roundNum, rollNum):
        if pool > (750 - rollNum * 10):
            return True
        return False


class RandomPlayer(Player):
    def banks(self, pool, roundNum, rollNum):
        if roundNum > 4 and random.randint(1, 6) == 6:
            return True
        return False


class R6Player(Player):
    def banks(self, pool, roundNum, rollNum):
        if roundNum > 6:
            return True
        return False


class R10Player(Player):
    def banks(self, pool, roundNum, rollNum):
        if roundNum > 10:
            return True
        return False


class R12Player(Player):
    def banks(self, pool, roundNum, rollNum):
        if roundNum > 12:
            return True
        return False
