import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "The 'or' can be achieved by taking the union of two regular expressions."
    ]

    data["params"]["language_description"] = \
        "All binary strings containing 010 or containing at least three 1s."
    
    server_base.generate(data)
