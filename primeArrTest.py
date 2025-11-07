cF=open("CorrectArr.txt","r")
tF=open("arraysave.txt","r")

correctArr = []
testArr =[]
f=open("arrErrors.txt","w")
for p in cF:
    correctArr.append(int(p))
for p in tF:
    testArr.append(int(p))

for i,num in enumerate(correctArr):
    if num == testArr[i]:
        continue
    else:
        f.write(f"{num} and {testArr[i]} failed at {i}\n")
f.close()
