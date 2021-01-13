import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "Consider the blocks of 1s that appear in the string. "
        "Unless a block is at the beginning or end of the string, then a certain restriction "
        "applies to the length of the block. What is this restriction?"
    ]

    data["params"]["language_description"] = \
        "All binary strings not containing the substring 010."
    
    server_base.generate(data)
