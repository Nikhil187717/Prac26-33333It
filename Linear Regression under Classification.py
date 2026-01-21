import numpy as np
import matplotlib.pyplot as plt

# Step 1: Sample dataset (Binary classification)
# X → input feature
# y → class labels (0 or 1)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype=float)

# Step 2: Mean values
X_mean = np.mean(X)
y_mean = np.mean(y)

# Step 3: Calculate coefficients (Slope m and Intercept c)
numerator = np.sum((X - X_mean) * (y - y_mean))
denominator = np.sum((X - X_mean) ** 2)

m = numerator / denominator
c = y_mean - m * X_mean

print("Slope (m):", m)
print("Intercept (c):", c)

# Step 4: Linear Regression prediction
y_pred = m * X + c

# Step 5: Classification using threshold
threshold = 0.5
y_class = [1 if value >= threshold else 0 for value in y_pred]

print("Predicted Values:", y_pred)
print("Predicted Classes:", y_class)

# Step 6: Visualization
plt.scatter(X, y, label="Actual Class", color='blue')
plt.plot(X, y_pred, label="Regression Line")
plt.axhline(y=threshold, linestyle='--', label="Threshold = 0.5")
plt.xlabel("X")
plt.ylabel("Class")
plt.legend()
plt.title("Linear Regression for Classification")
plt.show()
