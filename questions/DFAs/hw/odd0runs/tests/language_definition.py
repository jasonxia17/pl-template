def isInLanguage(x):
    return all(len(s) == 0 or len(s) % 2 == 1 for s in x.split('1'))

alphabet = ['0', '1']