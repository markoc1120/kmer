# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

# def test_me():
#    assert False, "Don't forget to write tests"


# I admit that I have been lazy with testing here, but
# the testing part was mostly an exercise and there isn't
# terribly much to test for these functions...

from kmer import (kmer, unique_kmers, count_kmers)


def test_kmer():
    assert kmer('', 3) == []
    assert kmer('agtagtcg', 3) == \
        ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']


def test_unique_kmers():
    assert unique_kmers('', 3) == []
    assert unique_kmers('agtagtcg', 3) == \
        ['agt', 'gta', 'tag', 'gtc', 'tcg']


def test_count_kmers():
    assert count_kmers('', 3) == {}
    assert count_kmers('agtagtcg', 3) == \
        {'agt': 2, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}
