import numpy as np

# Scenario 1: Add a zero at the end of a column matrix
A = np.array([[1], [2], [3]])
result1 = np.block([[A], [0]])
print("Scenario 1 (block):\n", result1)
# Output:
# [[1]
#  [2]
#  [3]
#  [0]]

# Scenario 2: Build a matrix [[A, 0], [C, 0]]
A = np.array([[1, 2], [3, 4]])
C = np.array([[5, 6]])
result2 = np.block([[A, np.zeros((2, 1))], [C, np.zeros((1, 1))]])
print("Scenario 2 (block):\n", result2)
# Output:
# [[1. 2. 0.]
#  [3. 4. 0.]
#  [5. 6. 0.]]

# Horizontal concatenation
B = np.array([[5, 6], [7, 8]])
hstack_result = np.hstack((A, B))
print("hstack:\n", hstack_result)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]

# Vertical concatenation
vstack_result = np.vstack((A, C))
print("vstack:\n", vstack_result)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# Append (vertical)
append_result = np.append(A, [[0, 0]], axis=0)
print("append:\n", append_result)
# Output:
# [[1 2]
#  [3 4]
#  [0 0]]

# Concatenate along the first dimension
concat_result1 = np.concatenate((A, C), axis=0)
print("concatenate (axis=0):\n", concat_result1)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# Concatenate along the second dimension
concat_result2 = np.concatenate((A, B), axis=1)
print("concatenate (axis=1):\n", concat_result2)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]
