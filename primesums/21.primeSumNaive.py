import time

def fullCheck(int, primes):
    for i,num in enumerate(primes):
        if int%num==0:
            return False
    return True

def segSeive(low, high, primes, limit):
    for i in range(low**2,high**2):
        if i>=limit:
            break
        elif i%2==0:
            continue
        elif i%low==0:
            continue
        elif fullCheck(i, primes):
            primes.append(i)
    return primes

def primeSearch(end):
    primes=[2,3,5,7,11,13,17,19,23,29]
    low=primes[0]
    highIndx = len(primes)-1
    high=primes[highIndx]
    i=0
    while i <= end:
        if high**2>=end:
            print(f"Finding primes between {low**2:,} and {end:,}")
        else:
            print(f"Finding primes between {low**2:,} and {high**2:,}")
        primes=segSeive(low,high,primes,end)
        low=high
        highIndx+=25
        high=primes[highIndx]
        i=low**2
    return primes
    

def main():
    end=int(input("What should the end of the prime search be? "))
    print(f"Finding all primes between 0 and {end:,}")
    start=time.process_time()
    primes=primeSearch(end)
    finish=time.process_time()
    secsTaken = round((finish-start)%60,2)
    minsTaken = int((finish-start)/60)
    print(f"{len(primes)} primes found in {minsTaken} minutes and {secsTaken} seconds")
    sum=0
    for i in primes:
        sum+=i
    print(f"Sum of primes from 0 to {end:,} is {sum:,}")

if __name__ == "__main__":
    main()