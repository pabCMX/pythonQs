from random import randint

def partition(arr, start, end, comp_func=lambda a,b : a >= b):
    pivot = arr[start]
    low = start+1
    high = end
    
    while True:
        while low <= high and comp_func(arr[high], pivot):
            high -= 1
        while low <= high and not comp_func(arr[low], pivot):
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high

def invPartition(arr, start, end, comp_func=lambda a,b : a <= b):
    pivot = arr[start]
    low = start+1
    high = end
    
    while True:
        while low <= high and comp_func(arr[high], pivot):
            high -= 1
        while low <= high and not comp_func(arr[low], pivot):
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    
    arr[high], arr[start] = arr[start], arr[high]
    return high

def quickSort(arr, start, end, inv=False, col=0):
    if start >= end:
        return
    if col > 0:
        if inv==True:
            pivot = invPartition(arr, start, end, lambda x, y : x[col] <= y[col])
            quickSort(arr,start,pivot-1,True, col=col)
            quickSort(arr,pivot+1, end, True, col=col)
        else:
            pivot = partition(arr, start, end, lambda x, y : x[col] >= y[col])
            quickSort(arr,start,pivot-1,col=col)
            quickSort(arr,pivot+1, end,col=col)
    else:
        if inv==True:
            pivot = invPartition(arr, start, end)
            quickSort(arr,start,pivot-1,True)
            quickSort(arr,pivot+1, end, True)
        else:
            pivot = partition(arr, start, end)
            quickSort(arr,start,pivot-1)
            quickSort(arr,pivot+1, end)
    
def countUnique(arr):
    returnArr = []
    count = 0
    tempArr = [arr[0]]
    for i in arr:
        for j,num in enumerate(tempArr):
            if i == num:
                count += 1
                break
            elif j == len(tempArr)-1:
                tempArr.append(count)
                returnArr.append(tempArr)
                tempArr = [i]
                count = 1
                break
    if count > 0:
        tempArr.append(count)
        returnArr.append(tempArr)
    return returnArr

def displayModes(arr,sort="Asc"):
    finalArr = []
    if sort == "Asc":
        quickSort(arr, 0, len(arr)-1,col=1)
    elif sort == "Dsc":
        quickSort(arr, 0, len(arr)-1,inv=True,col=1)
    
    for i in arr:
        for j in range (0,i[1]):
            finalArr.append(i[0])
    return finalArr

def main():
    f = open("listdump.txt","a")
    intList = []
    for i in range (0,200):
        intList.append(randint(0, 10))
    
    unsortedList = intList
    f.write(f"Here's the unsorted integer list:\n{intList}\n\n")

    quickSort(intList, 0, len(intList)-1)
    f.write(f"Here's the sorted ascending list:\n{intList}\n\n")

    quickSort(intList, 0, len(intList)-1,True)
    f.write(f"Here's the sorted decending list:\n{intList}\n\n")

    countOfInts = countUnique(intList)
    f.write(f"Here's the count of each integer:\n{countOfInts}\n\n")

    modeAscArr = displayModes(countOfInts)
    f.write(f"Here's the sorted mode Asc. count of each integer:\n{countOfInts}\n\n")
    f.write(f"Here's the sorted mode Asc. list:\n{modeAscArr}\n\n")

    modeDscArr = displayModes(countOfInts,"Dsc")
    f.write(f"Here's the sorted mode Dsc. count of each integer:\n{countOfInts}\n\n")
    f.write(f"Here's the sorted mode Dsc. list:\n{modeDscArr}\n\n")


    

if __name__ == "__main__":
    main()
