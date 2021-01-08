import numpy as np

if len(arr) % 5 != 0:
    arr = np.pad(arr, pad_width=(0, 5 - (len(arr) % 5)), constant_values=np.inf)

groups = arr.reshape(-1, 5)

medians = np.median(groups, axis=1)

pivot = np.median(medians)

left_side = []
right_side = []

for elem in arr:
    if elem <= pivot:
        left_side.append(elem)
    else:
        right_side.append(elem)

left_side = np.array(left_side)
right_side = np.array(right_side)

if k < len(left_side):
    next_arr = left_side
    next_k = k
else:
    next_arr = right_side
    next_k = k - len(left_side)
