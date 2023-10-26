import player
import game
import state_space


class RL_Player(player.Player):
    def __init__(self, name="default", discount=0.99, learningRate=0.1):
        self.score = 0
        self.name = name
        self.winCount = 0
        self.stateSpace = state_space.StateSpace(learningRate, discount, 10)
        self.isTrained = False

    def banks(self, pool, roundNum, rollNum):
        trueVal = self.stateSpace.getQuality(pool, roundNum, rollNum, True)
        falseVal = self.stateSpace.getQuality(pool, roundNum, rollNum, False)

        winningVal = trueVal >= falseVal
        if not self.isTrained:
            self.stateSpace.setNewQVal(pool, roundNum, rollNum, winningVal)

        return winningVal

    def train(self, view=False):
        trainingGame = game.Game([self])
        scores = []

        for i in range(10000):
            if i % 100 == 0 and i > 0 and view:
                print(f"After {i} rounds: ", sum(scores)/len(scores))
            trainingGame.play()
            scores.append(self.score)
            self.reset()
            trainingGame.resetGame()
        self.isTrained = True


def main():
    learningRate = 0.1
    discountRate = 0.99
    trainingPlayer = RL_Player("RL_Player", discountRate, learningRate)

    trainingPlayer.train(False)


if __name__ == "__main__":
    main()
