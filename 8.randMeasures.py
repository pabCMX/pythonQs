from random import randint

randArray = []
randCount = 3
max = 0
min = 20
sum = 0
avg = 0

for i in range (0,randCount):
    randArray.append(randint(0,20))

for j in randArray:
    if j>max:
        max=j
    if j<min:
        min=j
    sum+=j
avg = sum/len(randArray)

print("The {} random numbers are:".format(randCount))
print(randArray)
print("The max is: ")
print(max)
print("The min is: ")
print(min)
print("The avg is: ")
print(f"{avg:.3f}")
    
