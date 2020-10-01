#program to return century from year
def centuryFromYear(year):
    return year/100 if year%100==0 else int(year/100)+1
