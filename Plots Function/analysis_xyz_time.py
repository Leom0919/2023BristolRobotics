import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# Specify the path of the single CSV file you want to process
file_path = rf"E:\Dissertation\combination\20230716_checkeddata\July3_1\force_data_1.csv"

df = pd.read_csv(file_path)

# Convert the Timestamp to a recognizable datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

# Convert the datetime to a floating-point format that matplotlib can recognize
df['date_num'] = matplotlib.dates.date2num(df['Timestamp'])

# Create a new figure and 3D axis directly
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Create grid data
xi = np.linspace(df['Fx'].min(), df['Fx'].max(), 100)
yi = np.linspace(df['Fy'].min(), df['Fy'].max(), 100)
zi = griddata((df['Fx'], df['Fy']), df['Fz'], (xi[None,:], yi[:,None]), method='cubic')

# Interpolate for date_num
date_num_i = griddata((df['Fx'], df['Fy']), df['date_num'], (xi[None,:], yi[:,None]), method='cubic')

# Create a colormap
colors = plt.cm.viridis((date_num_i - df['date_num'].min()) / (df['date_num'].max() - df['date_num'].min()))

# Plot the data on the 3D plot
X, Y = np.meshgrid(xi, yi)
surf = ax.plot_surface(X, Y, zi, facecolors=colors, shade=False)
surf.set_facecolor((0,0,0,0))

ax.set_xlabel('Fx')
ax.set_ylabel('Fy')
ax.set_zlabel('Fz')

colorbar = plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
colorbar.set_label('Time (s)')
colorbar.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1])
colorbar.set_ticklabels(['0', '2', '4', '6', '8', '10'])

# Save the image and show it
image_path = file_path.replace('.csv', '.png')
plt.savefig(image_path)
plt.show()
