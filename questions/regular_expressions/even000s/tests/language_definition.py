def isInLanguage(x):
    counter = 0
    for i in range(len(x)):
        if x[i:i+3] == "000":
            counter += 1
    
    return counter % 2 == 0

alphabet = ['0', '1']