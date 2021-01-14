import regular_expressions.server_base as server_base

def generate(data):
    data["params"]["hints"] = [
        "Consider the graph of $y = \#_0(x) - \#_1(x)$ vs. the length of $x$. "
        "This graph goes up or down by 1 every time we append another symbol to $x$. "
        "Furthermore, the graph must stay between the horizontal lines $y=-2$ and $y=2$. "
        "Now, imagine we cut the graph into pieces every time it touches $y=0$. "
        "Then, each of those pieces must either be completely above the y-axis, or "
        "completely below the y-axis. Furthermore, each of those pieces, except for the last piece, "
        "must be balanced.",

        "Write a regular expression for all balanced strings where the graph of $y = \#_0(x) - \#_1(x)$ "
        "stays completely above the y-axis (except for the two endpoints, which touch the y-axis). "
        "Write another one for where the graph stays completely below the y-axis. Then, write two more "
        "for the same thing, except without the balanced restriction (i.e. it doesn't have to end "
        "on the y-axis).",
    ]

    data["params"]["language_description"] = \
        "All binary strings such that every prefix $x$ satisfies $|\#_0(x) - \#_1(x)| \le 2$."
    
    server_base.generate(data)
