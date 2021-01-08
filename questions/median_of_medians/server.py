import numpy as np


def generate(data):
    data["params"]["names_for_user"] = [
        {"name": "arr", "description": "The array of length $N$ to select from",
         "type": "1D numpy array"},

        {"name": "k", "description": "The rank to select ($0 \le k < N$)", "type": "int"}
    ]
    data["params"]["names_from_user"] = [
        {"name": "groups", "description": "The groups of 5",
         "type": "2D numpy array with shape $(\\lceil N/5 \\rceil, 5)$"},
        
        {"name": "medians", "description": "The medians of the groups",
         "type": "1D numpy array of length $\\lceil N/5 \\rceil$"},

        {"name": "pivot", "description": "The median of medians", "type": "float"},

        {"name": "left_side", "description": "All elements less than or equal to pivot",
        "type": "1D numpy array"},

        {"name": "right_side", "description": "All elements greater than pivot",
        "type": "1D numpy array"},

        {"name": "next_arr", "description": "The side to recurse into", "type": "1D numpy array"},
        {"name": "next_k", "description": "The value of k to use in the recursive call", "type": "int"}
    ]
