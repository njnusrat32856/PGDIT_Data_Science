import numpy as np

# 1. Creating Arrays
# 1D array
a = np.array([1, 2, 3])
print(a)  # [1 2 3]

# 2D array (matrix)
b = np.array([[1, 2], [3, 4]])
print(b)

# 2. Array Attributes
print(a.shape)   # (3,) → 1D array with 3 elements
print(b.shape)   # (2, 2) → 2 rows, 2 columns
print(b.ndim)    # 2 → 2-dimensional
print(b.dtype)   # int64 → data type

# 3. Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # [5 7 9]
print(a * b)  # [4 10 18]
print(np.sum(a))  # 6

# 4. Useful Functions
np.zeros((2, 3))     # 2x3 array of zeros
np.ones(5)           # 1D array of 5 ones
np.arange(0, 10, 2)  # [0 2 4 6 8]
np.linspace(0, 1, 5) # 5 numbers between 0 and 1

# 5. Random Numbers
np.random.seed(42)  # For reproducibility
np.random.rand(3)   # 3 random floats between 0 and 1

# array([6, 7, 8])

np.array([4, 5, 6])

np.random.seed(100)
arr_x = np.random.rand(10) * 100
# arr_x
print(arr_x)

mask = arr_x > 50
print(mask)

arr_x[mask]

print(arr_x[mask])



