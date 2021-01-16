import FAs.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "Every binary string except 000."
    
    server_base.generate(data)
