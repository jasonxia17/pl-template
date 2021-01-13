import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "All binary strings in which the number of 0s is 2 mod 3."
    
    server_base.generate(data)
