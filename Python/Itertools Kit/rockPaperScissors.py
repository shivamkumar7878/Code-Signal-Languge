from itertools import permutations

def rockPaperScissors(players):
    return sorted([list(x) for x in permutations(players,2)])
