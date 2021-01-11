def isInLanguage(x):
    return all(len(s) == 0 or len(s) >= 3 for s in x.split('1'))

alphabet = ['0', '1']