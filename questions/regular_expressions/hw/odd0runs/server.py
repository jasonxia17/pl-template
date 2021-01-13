import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "All binary strings in which every run of 0s has odd length."
    
    server_base.generate(data)
