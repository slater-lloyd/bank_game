import game
import player
import rl_player
from sys import argv


def getOtherPlayers():
    players = []
    players.append(player.RandomPlayer("RandomPlayer"))
    players.append(player.HundredPlayer("HundredPlayer"))
    players.append(player.OneFiftyPlayer("OneFiftyPlayer"))
    players.append(player.FiveHundredPlayer("FiveHundredPlayer"))

    return players


def getMLPlayer():
    return rl_player.RL_Player("QLearningPlayer")


def printHelpScript():
    script = """Welcome to Bank Game
    Use the following tags to start the game in the desired mode:
    -m : Start a game 1 on 1 with the machine learning opponent
    -g : Start a game with 4 other opponents with set strategies
    -t : Get output related to the machine learning player's training
    -s : Start a solo game. Try to maximize your own score"""

    print(script)


def trainML():
    ml = rl_player.RL_Player("QLearningPlayer")
    ml.train(True)


def main():
    if len(argv) == 1:
        printHelpScript()
        return 0

    players = []

    match argv[1]:
        case "-m":
            mlPlayer = getMLPlayer()
            mlPlayer.train()
            players.append(mlPlayer)
            players.append(player.UserPlayer("UserPlayer"))
        case "-g":
            players.extend(getOtherPlayers())
            players.append(player.UserPlayer("UserPlayer"))
        case "-t":
            trainML()
            return 0
        case "-s":
            players.append(player.UserPlayer("UserPlayer"))

    bank_game = game.Game(players, True)

    bank_game.play()

    if len(players) == 1:
        print(f"Final Score: {players[0].score}")
    else:
        for p in players:
            print(f"{p.name} - {p.score}")


if __name__ == "__main__":
    main()
