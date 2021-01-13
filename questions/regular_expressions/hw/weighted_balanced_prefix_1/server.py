import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "Try constructing the string one symbol at a time. "
        "What are the possible values of the first symbol? "
        "The first two symbols? The first three symbols? And so on..."
    ]

    data["params"]["language_description"] = \
        "All binary strings such that every prefix $x$ satisfies $|\#_0(x) - 2\cdot\#_1(x)| \le 1$."
    
    server_base.generate(data)
