import numpy as np

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5]).reshape(-1, 1)
print (X,y)
print(y.shape)
bias= np.ones((5,1))
print(bias)
X = np.hstack((bias, X))
print(X)
w= np.linalg.pinv(X) @ y
print(w)
y_pred = X @ w
print(y_pred)
loss = np.mean((y_pred - y) ** 2)
print(loss)
x_new = np.array([[1, 6]])  # include bias
y_new = x_new @ w

print(y_new)
