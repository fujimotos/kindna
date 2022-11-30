import sys
import collections
import itertools
import polyleven

def make_index(word, max_dist):
    """Return the set of index keys of a word.

    >>> make_index('aiu', 1)
    {'aiu', 'iu', 'au', 'ai'}
    """
    res = set()
    length = len(word)
    for dist in range(min(max_dist, length) + 1):
        variants = itertools.combinations(word, length - dist)
        for variant in variants:
            res.add(''.join(variant))
    return res

def main():
    groups = collections.defaultdict(set)
    for line in sys.stdin:
        dna = line.strip()
        for key in make_index(dna, 1):
            groups[key].add(dna)

    for grp in groups.values():
        for dna1, dna2 in itertools.combinations(grp, 2):
            dist = polyleven.levenshtein(dna1, dna2)
            if dist < 2:
                print("%s and %s is similar (dist=%i)" % (dna1, dna2, dist))

if __name__ == '__main__':
    main()
