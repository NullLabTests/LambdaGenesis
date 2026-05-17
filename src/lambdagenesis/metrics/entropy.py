from collections import Counter
from math import log2

def shannon_entropy(tokens):
    counts = Counter(tokens)

    total = sum(counts.values())

    if total == 0:
        return 0

    entropy = 0

    for value in counts.values():
        p = value / total
        entropy -= p * log2(p)

    return entropy
