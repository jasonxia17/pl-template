import CFGs.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "$$L = \{0^{2n}1^n \mid n \ge 0\}$$"
    
    server_base.generate(data)
