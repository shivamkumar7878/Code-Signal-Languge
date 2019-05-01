def first_bad_pair(sequence, k):
    """Return the first index of a pair of elements in sequence[]
    for indices k-1, k+1, k+2, k+3, ... where the earlier element is
    not less than the later element. If no such pair exists, return -1."""
    if 0 < k < len(sequence) - 1:
        if sequence[k-1] >= sequence[k+1]:
            return k-1
    for i in range(k+1, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    j = first_bad_pair(sequence, -1)
    if j == -1:
        return True  # List is increasing
    if first_bad_pair(sequence, j) == -1:
        return True  # Deleting earlier element makes increasing
    if first_bad_pair(sequence, j+1) == -1:
        return True  # Deleting later element makes increasing
    return False  # Deleting either does not make increasing
