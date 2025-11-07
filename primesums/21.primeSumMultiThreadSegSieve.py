import concurrent.futures
import time
import math

def initialCheck(i,arr,end):
    if arr[i]:
        print(f"Checking off multiples of {i}")
        for j in range(i**2,end, i):
                arr[j]=False

def segSieve(delta,sMult,pFactors):
    m = delta*sMult
    mMinus = m - delta
    arr = [True] * delta
    newPrimes = []
    print(f"Finding primes between {mMinus:,} and {m:,}.")
    for p in pFactors:
        start = math.ceil(mMinus/p)*p
        for j in range (start,m,p):
            indx = j-mMinus
            arr[indx] = False
    for i,pBool in enumerate(arr):
        if pBool:
            newPrimes.append(i+mMinus)
    return newPrimes

def primeSearch(end):
    #we first initialize the array with all Trues, up to the given limit.
    pFactors = []
    primes = []
    rootOfEnd = round(end**0.5)
    startArray = [True] * rootOfEnd
    startArray[0] = False
    startArray[1] = False
    for i in range (2,int(rootOfEnd**0.5)):
        initialCheck(i,startArray,rootOfEnd)
    for i,pBool in enumerate(startArray):
        if pBool:
            pFactors.append(i)
    primes.append(pFactors)
    with concurrent.futures.ThreadPoolExecutor(24) as executor:
        results = [
            executor.submit(
                segSieve,rootOfEnd,i,pFactors
            )
            for i in range (2,rootOfEnd+2)
        ]
    for arr in results:
        primes.append(arr)
    return primes

def primeSum(primes,end):
    sum = 0
    n=0
    for n in primes:
        if n>=end:
            break
        sum+=n
    return sum

def main():
    
    #end=int(input("What should the end of the prime search be? "))
    end=10**10

    print(f"Finding all primes between 0 and {end:,}")

    start = time.perf_counter()

    sum=primeSearch(end)

    finish = time.perf_counter()

    secsTaken = round((finish-start)%60,2)
    minsTaken = int((finish-start)/60)

    print(f"Finished prime search, all primes found in {minsTaken} minutes and {secsTaken} seconds.")
    print(f"Sum of primes from 0 to {end:,} is {sum:,}")

if __name__ == "__main__":
    main()