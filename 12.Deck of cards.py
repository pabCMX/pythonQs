from random import randint, randrange

def makeDeck():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    cards = ["King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace"]
    deck = []
    for s in suits:
        for c in cards:
            deck.append(f"{c} of {s}")
    return deck

def shuffle(arr):
    finalArr = arr
    tempArr = []
    randInd = randint(0, len(finalArr)-1)
    for _ in range (3):
        while len(finalArr)>0:
            tempArr.append(finalArr.pop(randInd))
            if len(finalArr) == 0:
                break
            randInd = randint(0, len(finalArr)-1)
        finalArr = tempArr
        tempArr = []
        randInd = randint(0, len(finalArr)-1)
    return finalArr
    
def draw(arr, amount):
    tempArr = []
    randCardInd = 0
    for _ in range (amount):
        randCardInd = randrange(0,len(arr)-1)
        tempArr.append(arr.pop(randCardInd))
    return tempArr

def main():
    deck = makeDeck()
    deck = shuffle(deck)
    drawnCards = draw(deck, 2)
    print(drawnCards)

if __name__ == "__main__":
    main()