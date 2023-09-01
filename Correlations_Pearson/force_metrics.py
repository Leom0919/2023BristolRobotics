import pandas as pd
from scipy.stats import pearsonr

# Texture attributes
data = {
    'Name': ["Felt", "Mesh", "Nylon", "Acrylic", "Fashion Fabric", "Fur", "Canvas", "Wool", "Cotton", "Wood"],
    'Traction': [2, 0, 2, 0, 0, 0, 1, 2.5, 1, -2],
    'Roughness': [2.5, -2, 3, -8, 2, 0.5, 4, 6, 3, -0.5],
    'Fineness': [-1.5, -3, 3, -9, 2, 2, 4, 5.5, 1, -2],
    'Hardness': [-6, 6, 5, 7, -1.5, -8, 5, -4, 0.5, 5],
    'Temperature': [2, 0, 0, -2, 0.5, 1, 0, 1, 0, 0]
}

attributes_df = pd.DataFrame(data)

# Force data
force_data = {
    'Name': ["Felt", "Mesh", "Nylon", "Acrylic", "Fashion Fabric", "Fur", "Canvas", "Wool", "Cotton", "Wood"],
    'Average Fz (N)': [-0.77, -0.84, -0.85, -0.65, -0.79, -0.57, -0.98, -0.98, -0.84, -0.89]
}
# 'Median Fz (N)': [0.63,0.61,0.74,0.49,0.59,0.43,0.79,0.77,0.67,0.7]
force_df = pd.DataFrame(force_data)

# Merge dataframes on 'Name'
merged_df = pd.merge(attributes_df, force_df, on='Name')

# Calculate Pearson correlation coefficients for each attribute with respect to 'Average Fz (N)'
correlations = {}
for attribute in ['Traction', 'Roughness', 'Fineness', 'Hardness', 'Temperature']:
    r_value, p_value = pearsonr(merged_df[attribute], merged_df['Average Fz (N)'])
    correlations[attribute] = (r_value, p_value)

print(correlations)
