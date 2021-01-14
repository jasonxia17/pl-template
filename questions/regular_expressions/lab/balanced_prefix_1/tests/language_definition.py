def isInLanguage(x):
    i = 0
    for c in x:
        if c == '0':
            i += 1
        else:
            i -= 1
        
        if abs(i) > 1:
            return False

    return True

alphabet = ['0', '1']