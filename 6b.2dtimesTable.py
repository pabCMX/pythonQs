multiTable = []
tempArr = []

for i in range (1,13):
    for j in range (1,13):
        tempArr.append(i*j)
    multiTable.append(tempArr)
    tempArr = []

for i in multiTable:
    for j in i:
        print(f"{j}",end="\t")
    print("")
