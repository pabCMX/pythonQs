import concurrent.futures
import sys
from bisect import bisect_right

import numpy as np


def sieve_base_primes(limit: int, dtype=np.uint64) -> np.ndarray:
    """Return all primes <= limit using a simple sieve (single-threaded)."""
    if limit < 2:
        return np.array([], dtype=dtype)

    # Inclusive limit
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[0:2] = False

    root = int(limit**0.5)
    for p in range(2, root + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 1 : p] = False

    return np.nonzero(is_prime)[0].astype(dtype)


def seg_sieve_worker(low: int, high: int, base_primes: np.ndarray, dtype) -> np.ndarray:
    """
    Sieve primes in [low, high), using provided base_primes (primes <= sqrt(global_end)).
    Designed to be called in separate processes.
    """
    if high <= low:
        return np.array([], dtype=dtype)

    size = high - low
    is_prime = np.ones(size, dtype=bool)

    # Vectorized marking for each base prime
    for p in base_primes:
        p = int(p)
        p2 = p * p
        if p2 >= high:
            break

        # First multiple of p in [low, high)
        start = (low + p - 1) // p * p
        if start < p2:
            start = p2
        if start >= high:
            continue

        is_prime[start - low : size : p] = False

    # Handle low == 0 / 1 explicitly if ever used
    if low == 0:
        if size > 0:
            is_prime[0] = False
        if size > 1:
            is_prime[1] = False

    segment_vals = np.arange(low, high, dtype=dtype)
    return segment_vals[is_prime]


class PrimeSearchSieve:
    def __init__(self, dtype=np.uint64):
        self.dtype = dtype

    def primeSearch(self, end: int, threads: int) -> np.ndarray:
        """
        Find all primes in [2, end], inclusive, using segmented sieve + multiprocessing.
        """
        if end < 2:
            return np.array([], dtype=self.dtype)

        # 1) Base primes up to sqrt(end)
        root = int(end**0.5)
        print("Finding initial prime factors.", end="")
        base_primes = sieve_base_primes(root, dtype=self.dtype)
        print("\tDone.")

        # 2) Segmented sieve over (root, end]
        print("Implementing full Sieve - Searching...", end="")

        # Choose segment size:
        # - Multiple of cache-friendly chunk
        # - Balanced vs process overhead
        # For 1e9, something like 1e6..5e6 is reasonable. We'll tie to root as you started.
        segment_size = max(root, 1_000_000)

        segments = []
        low = root + 1
        if low < 2:
            low = 2

        # We want to cover up to end inclusive, so high is exclusive: use end + 1
        limit = end + 1
        while low < limit:
            high = min(low + segment_size, limit)
            segments.append((low, high))
            low = high

        # 3) Parallel processing of segments
        primes_segments = [base_primes]

        if segments:
            with concurrent.futures.ProcessPoolExecutor(
                max_workers=threads
            ) as executor:
                futures = [
                    executor.submit(
                        seg_sieve_worker, low, high, base_primes, self.dtype
                    )
                    for (low, high) in segments
                ]
                for f in futures:
                    seg = f.result()
                    if seg.size > 0:
                        primes_segments.append(seg)

        print("\tDone.")

        # 4) Concatenate all
        print("Saving results.", end="")
        primes = np.concatenate(primes_segments)
        # Base primes and segment primes are naturally ordered by construction.
        print("\tDone.")

        return primes

    def primeSum(self, primes: np.ndarray, end: int) -> None:
        """
        Sum primes in [2, end], inclusive.
        Assumes 'primes' is sorted ascending.
        """
        # Last index with prime <= end
        count = bisect_right(primes, end)
        subset = primes[:count]
        total = int(subset.sum())
        print(f"Sum of {count:,} primes from 0 to {end:,} is {total:,}")


def main():
    import time

    end = 100000000000
    threads = 22

    print(f"Finding all primes between 0 and {end:,} (inclusive)")

    start = time.perf_counter()

    sieve = PrimeSearchSieve()
    primes = sieve.primeSearch(end, threads)
    if primes.size == 0:
        print("No primes found, exiting")
        sys.exit(1)

    finish = time.perf_counter()

    elapsed = finish - start
    mins = int(elapsed // 60)
    secs = round(elapsed % 60, 2)
    print(f"Finished prime search in {mins} minutes and {secs} seconds.")
    print(f"Now totaling all primes between 0 and {end:,} (inclusive)")
    sieve.primeSum(primes, end)


if __name__ == "__main__":
    main()
