# Bank Game

This is a text based version of the game "Bank". "Bank" is a game where players compete against other players to maximize their own score.

## Rules:
Each round, players take turns rolling a pair of dice. The sum of the value of the rolled dice is added to a "Pool". For example, if a player rolled 4 and 5, then 9 would be added to the Pool. The Pool resets to 0 each round. At any time, a player may "Bank" and add the current value of the Pool to their score. They then sit out the rest of the round. If the sum of the rolled dice ever equals 7, then the round is over and the pool resets. Players that have not Banked when the dice sum to 7 receive 0 points that round. A player may only Bank once per round. At the end of 15 rounds, the player with the highest score wins.

There are a few other rules to incentivize being risky:
1. If a player rolls doubles, then the Pool automatically doubles in value. If the pool was at 50 and a player rolled 1 and 1, then the pool would double and jump to 100.
2. For the first 3 rolls each round, 7s don't end the round and instead are added to the pool.

## Bots:
Playing alone is no fun. I've added a few bots to try your luck with. There are some that implement a certain strategy to maximize their earnings, others that play randomly, and one that implements a Q Learning algorithm. The Q Learning bot can be trained and played against for a difficult challenge.

## Run:
Use command: "python3 main.py" to run the game. It will give a list of tags to create a version of the game with opponents or for ML training.
