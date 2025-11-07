#22. Assume you are retrieving an array of integers. This array has size 1000 and is supposed to be filled with all the unique integers between 0 and 999 in random order. Unfortuately, we don't know if the array is actually full and we also know that one of the integers was repeated by mistake, while all the rest are unique. Find the repeat as efficiently as you can.
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def fileParse (file):
    f = open(file,'r')
    intList=[]
    intArrText=(f.read())
    tempNumText="" 
    for i,char in enumerate(intArrText):
        if char == "[":
            continue
        elif char == " " and tempNumText != "":
            intList.append(int(tempNumText))
            tempNumText = ""
        elif char =="]":
            break
        elif char != " ":
            tempNumText+=char
    return intList

def uniqSearch(intArr):
    uniqInts=[intArr[0]]
    rptInt=0
    fill=0   
    rptFound=False
    for i in intArr:
        if i == intArr[0]:
            continue

        elif not rptFound:
            for j in uniqInts:
                if j == i:
                    rptInt=i
                    rptFound=True
                    break
                elif j == uniqInts[len(uniqInts)-1] and j != i:
                    uniqInts.append(i)
                    break
                    
        elif rptFound:
            for j in uniqInts:
                if j == i:
                    fill=len(uniqInts)+1
                    return rptInt, fill
                elif j == uniqInts[len(uniqInts)-1] and j != i:
                    uniqInts.append(i)
                    break

def main():
    file = 'testArr.txt'
    intList = fileParse(file)
    intArr = np.asarray(intList)
    rptInt=0
    fill=0
    rptInt, fill = uniqSearch(intArr)
    f = open("checkedAns.txt","w")
    f.write(f"For {file} array, {rptInt} is repeated, and has {fill} numbers.\n{intArr}")

if __name__ == "__main__":
    main()