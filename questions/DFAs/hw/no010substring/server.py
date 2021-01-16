import FAs.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "Create a DFA that accepts strings containing 010. "
        "Then, take the complement of that DFA."
    ]

    data["params"]["language_description"] = \
        "All binary strings not containing the substring 010."
    
    server_base.generate(data)
