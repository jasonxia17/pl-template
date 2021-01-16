import FAs.server_base as server_base

def generate(data):
    data["params"]["hints"] = []

    data["params"]["language_description"] = \
        "All binary strings such that every prefix $x$ satisfies $|\#_0(x) - 2\cdot\#_1(x)| \le 7$."
    
    server_base.generate(data)
