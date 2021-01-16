def isInLanguage(x):
    if x == "":
        return True
    return int(x, 2) % 17 == 0

alphabet = ['0', '1']
