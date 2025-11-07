import time

def multiplesCheck(i, arr,end):
    if arr[i]:
            print(f"Checking off multiples of {i}")
            for j in range(i**2,end, i):
                    arr[j]=False

def primeSearch(end):
    #we first initialize the array with all Trues, up to the given limit.
    threads = []
    numArray = [True] * end
    numArray[0] = False
    numArray[1] = False
    for i in range (2,int(end**0.5)):
       multiplesCheck(i,numArray,end)
    return numArray

def primeSum(arr):
    sum=0
    for i,pBool in enumerate(arr):
        if pBool:
            sum+=i
    return sum
    
def main():
    
    end=10**9
    print(f"Finding all primes between 0 and {end}")
    start = time.perf_counter()
    primes=primeSearch(end)
    finish = time.perf_counter()
    secsTaken = round((finish-start)%60,2)
    minsTaken = int((finish-start)/60)
    print(f"Finished prime search, all primes found in {minsTaken} minutes and {secsTaken} seconds.")
    print(f"Now totaling all primes between 0 and {end}")
    sum=primeSum(primes)
    print(f"Sum of primes from 0 to {end:,} is {sum:,}")

if __name__ == "__main__":
    main()
#7,829,844KB