import pandas as pd
import os

root_directory = "E:/Dissertation/combination/20230716_checkeddata/"
texture_fz_averages = {f"Texture{i}_Avg_Force": 0 for i in range(1, 11)}
texture_counts = {f"Texture{i}_Avg_Force": 0 for i in range(1, 11)}

for directory, subdirs, files in os.walk(root_directory):
    for file in files:
        if file.startswith("force_data_") and file.endswith(".csv"):
            file_path = os.path.join(directory, file)
            df = pd.read_csv(file_path)

            # If the first force data is greater than 0, subtract it from all forces
            if df['Fz'].iloc[0] > 0:
                df['Fz'] -= df['Fz'].iloc[0]

            for i in range(1, 11):
                if f"force_data_{i}" in file:
                    texture_fz_averages[f"Texture{i}_Avg_Force"] += df['Fz'].mean()
                    texture_counts[f"Texture{i}_Avg_Force"] += 1

# Compute the actual average values
for key in texture_fz_averages:
    if texture_counts[key] > 0:
        texture_fz_averages[key] /= texture_counts[key]

# Print out the average values
for texture, avg_fz in texture_fz_averages.items():
    print(f"{texture}: {avg_fz:.2f}")
