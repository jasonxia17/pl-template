import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "Do casework on where the first 1 appears relative to the first two 0s.",

        "There should be three cases. "
        "The final answer should be the union of three regular expressions, one for each case.",
    ]

    data["params"]["language_description"] = \
        "All binary strings containing at least two 0s and at least one 1."
    
    server_base.generate(data)
