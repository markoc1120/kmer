from kmer import count_kmers, kmer, unique_kmers

# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_


def test_kmer():
    assert kmer("agtagtcg", 3) == ["agt", "gta", "tag", "agt", "gtc", "tcg"]


def test_unique_kmers():
    assert unique_kmers("agtagtag", 3) == ["agt", "gta", "tag"]


def test_count_kmers():
    assert count_kmers("agtagtag", 3) == {"agt": 2, "gta": 2, "tag": 2}
