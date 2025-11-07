testGrade = int(input("Enter your test grade: "))
projectIn = input("Did you do the project? Y/N ")
testLetter = 0

if testGrade >= 90 :
    testLetter = 1
elif testGrade >= 70:
    testLetter = 2
elif testGrade >= 50:
    testLetter = 3
else:
    testLetter = 4


if projectIn == "y" or projectIn == "Y":
    testLetter -= 1

if testLetter <= 1:
    print("You got an A!")
elif testLetter == 2:
    print("You got an B!")
elif testLetter == 3:
    print("You got an C.")
else:
    print("You got an F. Try harder.")
