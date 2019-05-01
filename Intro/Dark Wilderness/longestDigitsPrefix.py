def longestDigitsPrefix(inputString):
    import re
    prefix = inputString.split(" ")[0]
    if not prefix  or prefix.isdigit():
        return prefix
    elif prefix[0].isdigit():
        s = re.split('[a-z]+', inputString)
        return s[0]
    else:
        return ""
