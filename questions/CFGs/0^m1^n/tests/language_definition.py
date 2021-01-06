def generateLanguage(N):
    return {'0' * m + '1' * n for m in range(N + 1) for n in range(N + 1) if m != 2 * n and m + n <= N}