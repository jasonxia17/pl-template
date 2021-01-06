import fooling_sets.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "The strings in the fooling set should be prefixes of the strings in $L$."
    ]

    data["params"]["language_description"] = "$$L = \{0^n1^n \mid n \ge 0\}.$$"
    server_base.generate(data)
