import numpy as np
from scipy.stats import pearsonr

# Given data arrays
roughness = np.array([2.5, -2, 3, -8, 2, 0.5, 4, 6, 3, -0.5])
median_force = np.array([0.63,0.61,0.74,0.49,0.59,0.43,0.79,0.77,0.67,0.7])
touch_area = np.array([30.2910, 30.3991, 30.6004, 29.8116, 30.7124, 34.7645, 28.7475, 30.7335, 29.2751, 29.2061])
trajectory_length = np.array([17.410, 17.733, 17.447, 15.000, 17.208, 22.859, 16.748, 16.007, 17.111, 15.228])
hardness = np.array([-6, 6, 5, 7, -1.5, -8, 5, -4, 0.5, 5])

# Calculate correlations
corr_roughness_force, p_roughness_force = pearsonr(roughness, median_force)
corr_hardness_touch, p_hardness_touch = pearsonr(hardness, touch_area)
corr_hardness_trajectory, p_hardness_trajectory = pearsonr(hardness, trajectory_length)

# Print correlations
print(f"Correlation between Roughness and Median Force: {corr_roughness_force:.2f} with p-value: {p_roughness_force:.4f}")
print(f"Correlation between Hardness and Touch Area: {corr_hardness_touch:.2f} with p-value: {p_hardness_touch:.4f}")
print(f"Correlation between Hardness and Trajectory Length: {corr_hardness_trajectory:.2f} with p-value: {p_hardness_trajectory:.4f}")
