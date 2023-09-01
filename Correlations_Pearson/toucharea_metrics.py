import numpy as np
import scipy.stats as stats

# Tactile metrics data
textures = ["Felt", "Mesh", "Nylon", "Acrylic", "Fashion Fabric", "Fur", "Canvas", "Wool", "Cotton", "Wood"]
traction = [2, 0, 2, 0, 0, 0, 1, 2.5, 1, -2]
roughness = [2.5, -2, 3, -8, 2, 0.5, 4, 6, 3, -0.5]
fineness = [-1.5, -3, 3, -9, 2, 2, 4, 5.5, 1, -2]
hardness = [-6, 6, 5, 7, -1.5, -8, 5, -4, 0.5, 5]
temperature = [2, 0, 0, -2, 0.5, 1, 0, 1, 0, 0]

# Touch Area data
touch_area = [30291.0, 30399.1, 30600.4, 29811.6, 30712.4, 34764.5, 28747.5, 30733.5, 29275.1, 29206.1]

metrics = {
    'Traction': traction,
    'Roughness': roughness,
    'Fineness': fineness,
    'Hardness': hardness,
    'Temperature': temperature
}

# Calculate Pearson correlation for each metric with Touch Area
correlation_results = {}

for key, values in metrics.items():
    r, p_value = stats.pearsonr(values, touch_area)
    correlation_results[key] = (r, p_value)

print(correlation_results)
