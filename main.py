import game
import player


def getOtherPlayers():
    players = []
    players.append(player.RandomPlayer("RandomPlayer"))
    players.append(player.HundredPlayer("HundredPlayer"))
    players.append(player.OneFiftyPlayer("OneFiftyPlayer"))
    players.append(player.FiveHundredPlayer("FiveHundredPlayer"))

    return players


def main():
    players = []
    players.append(player.MainPlayer("MainPlayer"))
    players.extend(getOtherPlayers())

    bank_game = game.Game(players)

    for i in range(10000):
        bank_game.play()
        bank_game.resetGame()

    for p in players:
        print(f"{p.name} - {p.winCount}")


if __name__ == "__main__":
    main()
