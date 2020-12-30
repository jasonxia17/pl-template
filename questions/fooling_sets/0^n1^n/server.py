import fooling_sets.server_base as server_base

def generate(data):
    server_base.generate(data)

    data["params"]["hints"] = [
        "Here is a helpful hint to get you started.",
        "another useful hint"
    ]
