import numpy as np

arr = np.arange(0,11)

index_2 = arr[2]

slice = arr[1:5]

broadcast = arr[0:5] = 100

arr = np.arange(0,11)

arr_copy = arr.copy()

arr_copy[:] = 200

mat = np.array([[5,10,15], [20,25,30],[35,40,45]])

row0 = mat[0]

get_25 = mat[1,1]

get_15 = mat[0,2]

mat_slice = mat[:2,1:]

mat_slice_1 = mat[1:,:2]

# Conditional Selection

arr = np.arange(1,11)

bool_arr = arr > 4

arr[bool_arr]

# Short way of writing it
arr[arr>4]

less_then_8 = arr[arr<=8]
