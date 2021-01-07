import FAs.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "The binary representations of all nonnegative integers divisible by 17. " \
        "(Leading 0s are allowed, and an empty string should be interpreted as 0.)"
    
    server_base.generate(data)
