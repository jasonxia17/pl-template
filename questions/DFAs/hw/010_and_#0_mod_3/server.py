import FAs.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "All binary strings containing 010 where the total number of 0s is divisible by 3."
    
    server_base.generate(data)
