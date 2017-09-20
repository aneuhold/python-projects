import random

deck = range(1,53)

def shuffleDeck():
    random.shuffle(deck)

shuffleDeck()

playerHand = []
dealerHand = []

def dealCards():
    playerHand.append(deck[0])
    del deck[0]
    dealerHand.append(deck[0])
    del deck[0]
    playerHand.append(deck[0])
    del deck[0]
    dealerHand.append(deck[0])
    del deck[0]

dealCards()

cardDictionary = {
    1 : "A",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    10 : "10",
    11 : "J",
    12 : "Q",
    13 : "K",
    14 : "A",
    15 : "2",
    16 : "3",
    17 : "4",
    18 : "5",
    19 : "6",
    20 : "7",
    21 : "8",
    22 : "9",
    23 : "10",
    24 : "J",
    25 : "Q",
    26 : "K",
    27 : "A",
    28 : "2",
    29 : "3",
    30 : "4",
    31 : "5",
    32 : "6",
    33 : "7",
    34 : "8",
    35 : "9",
    36 : "10",
    37 : "J",
    38 : "Q",
    39 : "K",
    40 : "A",
    41 : "2",
    42 : "3",
    43 : "4",
    44 : "5",
    45 : "6",
    46 : "7",
    47 : "8",
    48 : "9",
    49 : "10",
    50 : "J",
    51 : "Q",
    52 : "K",
    }

def calculateCardAmount(hand):
    total = 0
    aceCount = 0
    for card in hand:
        if cardDictionary[card] == "A":
            total += 11
            aceCount += 1
        elif cardDictionary[card] == "J":
            total += 10
        elif cardDictionary[card] == "Q":
            total += 10
        elif cardDictionary[card] == "K":
            total += 10
        else:
            total += int(cardDictionary[card])
    while aceCount > 0 and total > 21:
        # This takes into account aces being 1 or 11
        total -= 10
        aceCount -= 1
    return total

def showFirstDeal():
    print("Dealer Hand: ")
    print(" Flipped Over ")
    print(" " + cardDictionary[dealerHand[1]])
    print("Player Hand: ")
    for i in playerHand:
        print(" " + cardDictionary[i] + " ")

def showFullDeal():
    print("Dealer Hand: ")
    for i in dealerHand:
        print(" " + cardDictionary[i] + " ")
    print("Player Hand: ")
    for i in playerHand:
        print(" " + cardDictionary[i] + " ")

def showPlayerDeal():
    print("Player Hand: ")
    for i in playerHand:
        print(" " + cardDictionary[i] + " ")

def dealerPlay():
    while calculateCardAmount(dealerHand) < 17:
        dealerHand.append(deck[0])
        del deck[0]

showFirstDeal()
gameOver = False

def checkOrHitFunc():
    global gameOver
    checkOrHit = raw_input("Check or hit?:")
    while not(checkOrHit.lower() == "hit" or checkOrHit.lower() == "check"):
        checkOrHit = raw_input("Please enter \"Check\" or \"Hit\": ")

    if checkOrHit.lower() == "hit":
        playerHand.append(deck[0])
        del deck[0]
        showPlayerDeal()
        if calculateCardAmount(playerHand) > 21:
            showFullDeal()
            print("Bust!")
            gameOver = True
    elif checkOrHit.lower() == "check":
        dealerPlay()
        showFullDeal()
        if calculateCardAmount(playerHand) > calculateCardAmount(dealerHand) or calculateCardAmount(dealerHand) > 21:
            print("You Win!!")
        else:
            print("You lost")
        gameOver = True

while gameOver == False:
    checkOrHitFunc()

