import concurrent.futures
import sys
from bisect import bisect_right
from math import ceil

import numpy as np


class PrimeSearchSieve:
    def __init__(self, dtype=np.uint64):
        self.dtype = dtype

    def lowestMultCeil(self, mMinus, p):
        return p * ceil(mMinus / p)

    def initCheck(self, end):
        rootOfEnd = ceil(end**0.5)
        startArray = np.full(shape=end, fill_value=True, dtype=bool)
        segment = np.arange(end, dtype=self.dtype)
        startArray[0] = False
        startArray[1] = False
        for i in range(2, rootOfEnd):
            if startArray[i]:
                startArray[i**2 :: i] = False
        pFactors = segment[startArray]
        return pFactors

    def segSieve(self, delta, sMult, pFactors):
        m = delta * sMult
        mMinus = m - delta
        testArr = np.full(shape=delta, fill_value=True, dtype=bool)
        segment = np.arange(mMinus, m, dtype=self.dtype)
        for p in pFactors:
            Start = int(self.lowestMultCeil(mMinus, p))
            testArr[Start - mMinus :: p] = False

        primes = segment[testArr]
        return primes

    def primeSearch(self, end, threads):
        if end < 2:
            return []
        rootOfEnd = ceil(end**0.5)
        print("Finding intial prime factors.", end="")
        pFactors = self.initCheck(rootOfEnd)
        print("\tDone.")
        print("Implementing full Sieve - Searching...", end="")
        with concurrent.futures.ProcessPoolExecutor(threads) as executor:
            futures = [
                executor.submit(self.segSieve, rootOfEnd, i, pFactors)
                for i in range(2, rootOfEnd + 1)
            ]
        print("\tDone.")

        print("Saving results.", end="")
        primesList = []
        primes = np.ndarray(1, dtype=object)
        primes[0] = pFactors
        for future in futures:
            primesList.append(future.result())
        primes = np.append(primes, primesList)
        primes = np.hstack(primes)
        print("\tDone.")
        return primes

    def primeSum(self, primes, end):
        count = bisect_right(primes, end)
        sum = np.sum(primes, where=primes < end)
        print(f"Sum of {count:,} primes from 0 to {end:,} is {int(sum):,}")


def main():
    import time

    end = 10**9
    threads = 22
    print(f"Finding all primes between 0 and {end:,}")

    start = time.perf_counter()

    pSieve = PrimeSearchSieve()
    primes = pSieve.primeSearch(end, threads)
    if len(primes) == 0:
        print("No primes found, exiting")
        sys.exit()

    finish = time.perf_counter()

    secsTaken = round((finish - start) % 60, 2)
    minsTaken = int((finish - start) / 60)
    print(f"Finished prime search in {minsTaken} minutes and {secsTaken} seconds.")
    print(f"Now totaling all primes between 0 and {end:,}")
    pSieve.primeSum(primes, end)


if __name__ == "__main__":
    main()
