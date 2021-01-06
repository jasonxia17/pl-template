import CFGs.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "Extend the previous grammar. What is missing?",

        "We can express $L$ as $$L = \{0^m1^n \mid m \\neq 2n\} \cup X.$$"
        "What is $X$? How would we generate $X$ with a CFG?"
    ]

    data["params"]["language_description"] = \
        "$$L = \{0,1\}^* \setminus \{0^{2n}1^n \mid n \ge 0\}$$"
    
    server_base.generate(data)
