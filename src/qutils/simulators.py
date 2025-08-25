from typing import Dict, Iterable


def shots_to_counts(bits: Iterable[Iterable[int]]) -> Dict[str, int]:
    """Convert bitstrings (iterables of 0/1 values) into a dict of counts."""
    counts: Dict[str, int] = {}
    for b in bits:
        s = "".join(str(bit) for bit in b)
        counts[s] = counts.get(s, 0) + 1
    return counts
