import fooling_sets.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "Here is a helpful hint to get you started.",
        "another useful hint",
        "<a href=\"/\">link</a> $x^2$"
    ]

    data["params"]["language_description"] = "$$L = \{0^n1^n \mid n \ge 0\}.$$"
    server_base.generate(data)
