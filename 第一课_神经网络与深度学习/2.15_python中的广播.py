import numpy as np

# create a 3x4 array
A = np.array([
    [56.0, 0.0, 4.4, 68.0],
    [1.2, 104.0, 52.0, 8.0],
    [1.8, 135.0, 99.0, 0.9]
])

print(A)

# axis=0 equals 0 means to sum vertically 竖直
# axis=0 equals 0 means to sum horizontally 水平
cal = A.sum(axis=0)

print(cal)

# Broadcasting (1x4) auto-expand to (3x4)
percentage = 100 * A/cal.reshape(1, 4)
print(percentage)
