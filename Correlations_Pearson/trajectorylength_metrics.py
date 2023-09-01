import numpy as np
from scipy.stats import pearsonr

# Trajectory lengths for each texture
trajectory_length = np.array([1741.0, 1773.3, 1744.7, 1500.0, 1720.8,
                              2285.9, 1674.8, 1600.7, 1711.1, 1522.8])

# Tactile metrics for each texture
traction = np.array([2, 0, 2, 0, 0, 0, 1, 2.5, 1, -2])
roughness = np.array([2.5, -2, 3, -8, 2, 0.5, 4, 6, 3, -0.5])
fineness = np.array([-1.5, -3, 3, -9, 2, 2, 4, 5.5, 1, -2])
hardness = np.array([-6, 6, 5, 7, -1.5, -8, 5, -4, 0.5, 5])
temperature = np.array([2, 0, 0, -2, 0.5, 1, 0, 1, 0, 0])

# Compute Pearson correlations
correlations = {
    'Traction': pearsonr(trajectory_length, traction),
    'Roughness': pearsonr(trajectory_length, roughness),
    'Fineness': pearsonr(trajectory_length, fineness),
    'Hardness': pearsonr(trajectory_length, hardness),
    'Temperature': pearsonr(trajectory_length, temperature)
}

# Print the correlations
for metric, (r, p) in correlations.items():
    print(f"{metric}: r = {r:.3f}, p-value = {p:.3f}")

