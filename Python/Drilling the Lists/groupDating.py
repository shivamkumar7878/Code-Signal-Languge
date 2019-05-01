def groupDating(male, female):
    return zip(*[[m, f] for (m, f) in zip(male, female) if m != f])
