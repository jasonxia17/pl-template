import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "Any string in the language can be expressed as $x010y$. "
        "Perform casework on the value of $\#_0(x) \\bmod 3$.",

        "The value of $\#_0(x) \\bmod 3$ uniquely determines the value of $\#_0(y) \\bmod 3$.",

        "The final answer should be the union of three regular expressions, one for each case.",

        "Let $L_i = \{x \mid \#_0(x) \equiv i \\pmod 3\}$. Write regular expressions for "
        "$L_0$, $L_1$, and $L_2$, and use those as subexpressions to compose the final answer."
    ]

    data["params"]["language_description"] = \
        "All binary strings containing 010 where the total number of 0s is divisible by 3."
    
    server_base.generate(data)
