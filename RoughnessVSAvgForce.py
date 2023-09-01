import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Convert lists to numpy arrays
Roughness_ratings = np.array([2.5, -2, 3, -8, 2, 0.1, 3.9, 6, 3.5, -0.5]).reshape(-1, 1)
avg_forces = np.array([-0.94, -1.00, -0.95, -0.78, -0.91, -0.66, -1.09, -1.08, -0.93, -1.00])

# Create and fit linear regression model
model_linear = LinearRegression()
model_linear.fit(Roughness_ratings, avg_forces)

# Generate prediction for linear model
x_range = np.linspace(-10, 10, 100).reshape(-1, 1)
y_range_linear = model_linear.predict(x_range)

# Plotting
plt.figure(figsize=(10, 5))
plt.scatter(Roughness_ratings, avg_forces, color='blue')
plt.plot(x_range, y_range_linear, color='red')
plt.title('Linear Regression')
plt.xlabel('Roughness Rate (-10: very smooth, +10: very rough)')
plt.ylabel('Average Force\n("-" Sign Indicates Downward Direction)')
plt.xlim(-10, 10)
plt.ylim(0, -1.2)

plt.tight_layout()
plt.show()
