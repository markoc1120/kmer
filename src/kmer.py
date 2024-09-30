from collections import Counter

"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """
    return [x[i : i + k] for i in range(len(x) - k + 1)]


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    >>> unique_kmers('agtagtag', 3)
    ['agt', 'gta', 'tag']

    FIXME: do you want more tests here?
    """
    seen, ans = set(), []
    for i in range(len(x) - k + 1):
        curr = x[i : i + k]
        if curr in seen:
            continue
        ans.append(curr)
        seen.add(curr)
    return ans


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('agtagtag', 3)
    Counter({'agt': 2, 'gta': 2, 'tag': 2})

    FIXME: do you want more tests here?
    """
    counter = Counter()
    for i in range(len(x) - k + 1):
        counter[x[i : i + k]] += 1
    return counter
