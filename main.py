import numpy as np
# import matplotlib.pyplot as plt


# def step_function(x):
#     return np.array(x > 0, dtype=np.int)


# def sigmoid(x):
#     print(np.exp(-x))
#     return 1 / (1 + np.exp(-x))


# def relu(x):
#     return np.maximum(0, x)


# x = np.arange(-5.0, 5.0, 0.1)
# y = relu(x)
# plt.plot(x, y)
# plt.ylim(-1, 5.1)
# plt.show()

# A = np.array([1, 2, 3, 4])
A = np.array([[1, 2, 4], [3, 4, 5]])
B = np.array([[1, 3], [3, 4], [5, 6]])

print(np.dot(A, B))
