import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "All binary strings containing the substring 000."
    
    server_base.generate(data)
