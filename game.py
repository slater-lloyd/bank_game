import random


class Game:
    def __init__(self, players):
        self.players = players
        self.inPlay = players.copy()
        self.pool = 0
        self.roundNum = 0
        self.rollNum = 0
        self.bust = False

    def play(self):
        while self.roundNum < 15:
            # roll dice
            rolls = self.getDiceRolls()
            self.rollNum += 1
            sum = rolls[0] + rolls[1]
            # compute rules
            if self.rollNum <= 3 and sum == 7:
                self.pool += 70
            elif self.rollNum <= 3:
                self.pool += sum
            elif sum == 7:
                self.bust = True
            elif rolls[0] == rolls[1]:
                self.pool *= 2
            else:
                self.pool += sum

            if not self.bust:
                for player in self.inPlay:
                    if player.banks(self.pool, self.roundNum, self.rollNum):
                        player.add(self.pool)
                        self.inPlay.remove(player)
                if len(self.inPlay) == 0:
                    self.resetRound()
            elif self.bust:
                self.resetRound()
        return self.winner()

    def resetGame(self):
        self.pool = 0
        self.playerScores = []
        self.roundNum = 0
        self.rollNum = 0
        self.bust = False
        for player in self.players:
            player.reset()
        self.inPlay = self.players.copy()

    def resetRound(self):
        self.pool = 0
        self.rollNum = 0
        self.bust = False
        self.inPlay = self.players.copy()
        self.roundNum += 1

    def getDiceRolls(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return (dice1, dice2)

    def winner(self):
        topScore = 0
        topPlayer = None
        for player in self.players:
            if player.score > topScore:
                topScore = player.score
                topPlayer = player
        if topPlayer:
            topPlayer.won()
        return topPlayer

    def getPlayers(self):
        return self.players


def main():
    tester = Game(None)

    count = 0
    for i in range(600):
        rolls = tester.getDiceRolls()
        if rolls[0] + rolls[1] == 7:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
