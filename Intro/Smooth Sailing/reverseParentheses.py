def reverseParentheses(s):
    from collections import Counter
    for i in range(Counter(s)['(']):
        one = s.rsplit('(',1)
        print(one)
        two = one[1].split(')',1)
        print(two)
        s = one[0]+two[0].replace(two[0],two[0][::-1]+two[1])
        print(s)
    return s 
