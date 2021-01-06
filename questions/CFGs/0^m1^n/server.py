import CFGs.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "If $m \\neq 2n$, then either $m < 2n$ or $m > 2n$. Write a CFG for each of the cases separately, "
        "then take the union of the two CFGs."
    ]

    data["params"]["language_description"] = \
        "$$L = \{0^m1^n \mid m \\neq 2n\}$$"
    
    server_base.generate(data)
