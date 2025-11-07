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

    def initCheck(self, limit):
        # moved limit check here given namesake
        if limit < 2:
            return np.array([], dtype=self.dtype)

        root = int(limit**0.5) + 1
        # limit is now inclusive
        is_prime = np.full(limit + 1, True, dtype=bool)
        # removed unnecessary extra range given we can convert using np.nonzero at end
        is_prime[0:2] = False
        # range is also inclusive
        for p in range(2, root + 1):
            if is_prime[p]:
                start = p * p
                if start > limit:
                    break
                # python slicing, also needs explicit inclusivity
                is_prime[start : limit + 1 : p] = False

        primes = np.nonzero(is_prime)[0].astype(self.dtype)
        return primes

    def segSieve(self, low, high, pFactors):
        # checking for nonzero size of segment
        size = max(0, high - low)
        if size <= 0:
            return np.array([], dtype=self.dtype)

        is_prime = np.full(size, True, dtype=bool)

        for p in pFactors:
            p = int(p)
            if p * p > high:
                break

            # First multiple of p in [low, high)
            start = (low + p - 1) // p * p
            if start < p * p:
                start = p * p
            if start >= high:
                continue

            is_prime[start - low : size : p] = False

        # Exclude 0 and 1 if they fall into first segment
        if low == 0:
            if size > 0:
                is_prime[0] = False
            if size > 1:
                is_prime[1] = False

        return (np.arange(low, high, dtype=self.dtype))[is_prime]

    def primeSearch(self, end, threads):
        if end < 2:
            return np.array([], dtype=self.dtype)

        root = int(end**0.5)
        print("Finding intial prime factors.", end="")
        pFactors = self.initCheck(root)
        print("\tDone.")

        print("Implementing full Sieve - Searching...", end="")

        # Choose segment size
        delta = root  # reasonable; can be tuned

        # Build list of [low, high) segments covering [2, end)
        # First segment will also contain some primes already in pFactors.
        # To avoid duplication, we ensure first segment starts at max(2, root+1)

        # So adjust:
        segments = []
        low = root + 1
        if low < 2:
            low = 2
        # Using end + 1 to cover 'end' inclusively
        limit = end + 1
        while low < limit:
            high = min(low + delta, limit)
            segments.append((low, high))
            low = high

        with concurrent.futures.ProcessPoolExecutor(threads) as executor:
            futures = [
                executor.submit(self.segSieve, low, high, pFactors)
                for (low, high) in segments
            ]

        print("\tDone.")

        print("Saving results.", end="")
        primes_segments = [pFactors]
        for future in futures:
            seg = future.result()
            if seg.size > 0:
                primes_segments.append(seg)

        primes = np.concatenate(primes_segments).astype(self.dtype)
        print("\tDone.")
        return primes

    def primeSum(self, primes, end):
        count = bisect_right(primes, end)
        subset = primes[:count]
        total = int(subset.sum())
        print(f"Sum of {count:,} primes from 0 to {end:,} is {total:,}")


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
