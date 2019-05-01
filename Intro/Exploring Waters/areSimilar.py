def areSimilar(a, b):

    return sorted(a)==sorted(b) and sum([A!=B for A,B in zip(a,b)])<=2
