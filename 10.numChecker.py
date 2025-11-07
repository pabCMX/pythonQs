from random import randint

randArray = []
randCount = 100
usrNum = int(input("Enter a number to check: "))
usrConfirm = "Y"
numExists = bool(0)
usrContinue = bool(1)

for i in range(0, randCount):
    randArray.append(randint(0, 10001))

while usrContinue:
    for t in randArray:
        if t == usrNum:
            numExists = 1
    if numExists:
        print("{} is in the list".format(usrNum))
        numExists = 0
    else:
        print("{} is NOT in the list".format(usrNum))
    usrConfirm = input("Would you like to search again? Y/N ")
    if usrConfirm == "Y" or usrConfirm == "y":
        usrContinue = 1
        usrNum = int(input("Enter a number to check: "))
    else:
        usrContinue = 0
    
    