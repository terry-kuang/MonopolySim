from random import randint

dice1 = -1
dice2 = -1
total = 0
game = True
double = True
position = 0
turn = 0
totalDoubles = 0
cardChance = -1

while game is True:
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    total = dice1 + dice2

    turn += 1
    print("Turn:", turn)

    # Position of Player
    position += total

    if position > 39:
        position = position - 40

    print("Position:", position)

    print("Total:", total, "Dice 1:", dice1, "Dice 2:", dice2)

    # Landing on Community Chest or Chance
    if position == 2 or 7 or 22 or 33 or 36:
        cardChance = randint(1, 16)
        if cardChance == 8:
            position = 10
            print("Player has been sent to jail by drawing a chance/community chest card")

    # User Throws a Double
    if dice1 == dice2:
        double = True
        totalDoubles += 1
        print("Doubles Thrown:", totalDoubles)
    else:
        double = False
        totalDoubles = 0

    # Player Caught Speeding (Rolling 3 consecutive Doubles)
    if totalDoubles == 3:
        print("Player has been sent to jail due to speeding")
        position = 10

    # Landing on Pos. 30 (Go to Jail Tile)
    if position == 30:
        position = 10
        print ("Player has been sent to jail due to landing on Pos.30")

    # Game Limit
    if turn == 3:
        game = False




