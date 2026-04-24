"""
NUMPY PRACTICE TEST — QUESTIONS + ANSWERS

Covers:
- Broadcasting
- Axis operations
- Indexing & filtering
- Reshaping
- Matrix multiplication
- Vectorization
- Aggregations
"""

import numpy as np

# -----------------------------
# Q1 — Broadcasting
# -----------------------------
A = np.arange(12).reshape(3,4)
B = np.array([1,2,3,4])

C = A + B
print("Q1 Output:\n", C)
print("Shape:", C.shape)
# Explanation: B (4,) is broadcast across rows of A (3,4)


# -----------------------------
# Q2 — Axis understanding
# -----------------------------
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

sum_axis0 = np.sum(A, axis=0)
sum_axis1 = np.sum(A, axis=1)

print("\nQ2 axis=0 (column sums):", sum_axis0)  # [12 15 18]
print("Q2 axis=1 (row sums):", sum_axis1)      # [ 6 15 24]


# -----------------------------
# Q3 — Indexing + logic
# -----------------------------
A = np.array([10, 15, 20, 25, 30])

div_by_10 = A[A % 10 == 0]
range_vals = A[(A >= 15) & (A <= 30)]

print("\nQ3 divisible by 10:", div_by_10)   # [10 20 30]
print("Q3 between 15 and 30:", range_vals) # [15 20 25 30]


# -----------------------------
# Q4 — Reshape
# -----------------------------
A = np.arange(24)

reshaped_1 = A.reshape(4,6)
reshaped_2 = A.reshape(2,4,3)  # since 2 * 4 * 3 = 24

print("\nQ4 reshape (4,6):\n", reshaped_1)
print("Q4 reshape (2,4,3):\n", reshaped_2)


# -----------------------------
# Q5 — Matrix multiplication
# -----------------------------
A = np.random.rand(3,2)
B = np.random.rand(2,4)
C = np.random.rand(3,4)

print("\nQ5 Valid operations:")
print("A @ B shape:", (A @ B).shape)  # (3,4)

# Invalid:
# B @ A → not valid (4 ≠ 3)
# A @ C → not valid (2 ≠ 3)


# -----------------------------
# Q6 — Vectorization
# -----------------------------
A = np.array([1,2,3,4])

A[A % 2 == 0] = 0

print("\nQ6 replace evens with 0:", A)  # [1 0 3 0]


# -----------------------------
# Q7 — Mean of columns
# -----------------------------
A = np.array([[1,2],
              [3,4],
              [5,6]])

col_mean = np.mean(A, axis=0)

print("\nQ7 column means:", col_mean)  # [3. 4.]
print("Shape:", col_mean.shape)        # (2,)


# -----------------------------
# END
# -----------------------------