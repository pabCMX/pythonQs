from random import randint
for i in range (0,100):
    randSecs = randint(0, 10000)
    randMins = 0

    unfmtSecs = randSecs%60

    randMins = int((randSecs-unfmtSecs)/60)
    unfmtMins = randMins%60

    unfmtHrs = int((randMins-unfmtMins)/60)

    print(f"Rand secs are {randSecs:5}; formatted time is {unfmtHrs}:{unfmtMins:02}:{unfmtSecs:02}")