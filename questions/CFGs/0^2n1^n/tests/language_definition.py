def generateLanguage(N):
    return {'0' * (2 * n) + '1' * n for n in range(N // 3 + 1)}