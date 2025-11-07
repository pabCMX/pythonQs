#22. Assume you are retrieving an array of integers. This array has size 1000 and is supposed to be filled with all the unique integers between 0 and 999 in random order. Unfortuately, we don't know if the array is actually full and we also know that one of the integers was repeated by mistake, while all the rest are unique. Find the repeat as efficiently as you can.
import numpy as np
from random import randint
import sys
np.set_printoptions(threshold=sys.maxsize)



intArray=np.zeros(1000,dtype=np.uint32)
fillIndx=randint(350,1000)
repeatChance=5
repeatCheck=False
repeatContinue=False
repeatedInt=0
randAvailInt=randint(0,999)
availableInts = np.arange(0,1000,1)

for i in range(fillIndx-2):
    if len(availableInts)<=1:
        #if we run out of available Ints, then we had to fill the whole array
        # and therefore, we use the last availableInt, and end with an empty
        # array. The loop will stop by hitting the fillIndx limit as normal.
        intArray[i]=availableInts[randAvailInt]
        availableInts=np.delete(availableInts,randAvailInt)
        continue

    elif repeatCheck or repeatChance<randint(0,100):
        #choose int as normal and continue
        intArray[i]=availableInts[randAvailInt]
        availableInts=np.delete(availableInts,randAvailInt)
        randAvailInt=randint(0,len(availableInts)-1)

    elif not repeatCheck:
        #set repeatflags, save the repeated int, and choose another int
        # normally.
        repeatCheck=True
        repeatContinue=True
        repeatedInt=availableInts[randAvailInt]
        availableInts=np.delete(availableInts,randAvailInt)
        randAvailInt=randint(0,len(availableInts)-1)
        #choosing int normally.
        intArray[i]=availableInts[randAvailInt]
        availableInts=np.delete(availableInts,randAvailInt)
        randAvailInt=randint(0,len(availableInts)-1)

#Finally randomly insert the repeated ints throughout the list.
for i in range(2):
    intArray=np.insert(intArray,randint(0,fillIndx-(2-i)),repeatedInt)
f = open(f'testArr.txt','w')
f.write(f"{intArray}\n")
f.close()
ans = open(f'ansArr.txt','w')
ans.write(f"Rep int is {repeatedInt}, {fillIndx} full.\n{intArray}\n")
ans.close()