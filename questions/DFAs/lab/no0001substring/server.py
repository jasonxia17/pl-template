import FAs.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "All binary strings in which 1 does not appear after a substring 000."
    
    server_base.generate(data)
