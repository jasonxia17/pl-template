import FAs.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "For what values of $n$ does the substring $000$ appear in $0^n$ an odd number of times?",

        "Consider the maximal blocks of 0s that appear in a string. For example, in $10001101110000100000$, "
        "the maximal blocks of 0s are $$1(000)11(0)111(0000)1(00000).$$"
        "Then, consider the number of occurrences of $000$ contributed by each block.",

        "Some of these blocks contribute an odd number of occurrences of $000$. We want those "
        "types of blocks to appear an even number of times."
    ]

    data["params"]["language_description"] = \
        "All binary strings in which the substring $000$ appears an even number of times."
    
    server_base.generate(data)
