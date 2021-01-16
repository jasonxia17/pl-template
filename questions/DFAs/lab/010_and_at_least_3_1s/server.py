import FAs.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "All binary strings containing at least two 0s and at least one 1."
    
    server_base.generate(data)
