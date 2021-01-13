import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "There must be two more 1s in addition to the 1 that appears in 010. "
        "Do casework on where those two 1s appear relative to the 010 substring.",

        "There should be three cases. "
        "The final answer should be the union of three regular expressions, one for each case.",

        "The two 1s can both appear before 010, both after, or one before and one after."
    ]

    data["params"]["language_description"] = \
        "All binary strings containing 010 and containing at least three 1s."
    
    server_base.generate(data)
