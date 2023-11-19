# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def k_nn_regression(X_train, y_train, X_test, k):
    knn_reg = KNeighborsRegressor(n_neighbors=k)
    knn_reg.fit(X_train, y_train)
    y_pred = knn_reg.predict(X_test)
    return y_pred, knn_reg.score(X_test, y_test)

# input n
N = int(input("enter a number of data points n "))

# input k
k = int(input("enter the value of k (k <= N) "))
if k > N:
    print("k should be less or equal to N.")
    exit()

# input x, y
X_data = []
y_data = []
for i in range(N):
    x_value = float(input(f"enter X  for point {i+1} "))
    y_value = float(input(f"enter Y  for point {i+1} "))
    X_data.append(x_value)
    y_data.append(y_value)

# lists to numpy arrays
X_data = np.array(X_data).reshape(-1, 1)
y_data = np.array(y_data)

# input x value for prediction
X_input = float(input("enter x value for prediction "))
X_test = np.array([[X_input]])

# k-nn regression
y_pred, r2_coefficient = k_nn_regression(X_data, y_data, X_test, k)

#  result of k-nn regression
print(f" k-nn regression {y_pred[0]}")

# coefficient of determination (R-squared)
print(f"coefficient of determination (R-squared) {r2_coefficient}")

# -


