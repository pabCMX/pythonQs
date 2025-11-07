usrSentence = input("Please input your sentence: \n")
delimiter = input("Please input the delimiter: ")
letterArr = []
wordArr = []

for i,char in enumerate(usrSentence):
    if char == delimiter:
        wordArr.append(letterArr)
        letterArr = []
    elif i == len(usrSentence):
        wordArr.append(letterArr)
        letterArr = []
    else:
        letterArr.append(char)

for j in wordArr:
    for k in j:
        print(k,end="")
    print()