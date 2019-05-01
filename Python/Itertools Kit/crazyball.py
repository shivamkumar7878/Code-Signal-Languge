from itertools import combinations

def crazyball(players, k):
    return [list(x) for x in sorted(combinations(sorted(players),k))]
