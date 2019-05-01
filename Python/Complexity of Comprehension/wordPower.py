def wordPower(word):
    num = {letter: string.ascii_lowercase.find(letter)+1 for letter in word}
    return sum([num[ch] for ch in word])
