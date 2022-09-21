from __future__ import annotations
from collections import Counter

def nonDivisibleSubset(k:int , s: list[int]) -> int:
    c = Counter([ss % k for ss in s])
    n = sum(max(c[i], c[k-i]) for i in range(1, k//2 + k%2))
    return n + (0 in c) + (k%2 == 0 and k/2 in c)