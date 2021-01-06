import itertools

def generateLanguage(N):
    return {"".join(chars) for l in range(N + 1) for chars in itertools.product("01", repeat=l)} \
                .difference({'0' * (2 * n) + '1' * n for n in range(N // 3 + 1)})