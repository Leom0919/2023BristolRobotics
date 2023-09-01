import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

def plot_3d_graph(ax, file_path):
    df = pd.read_csv(file_path)

    # Convert the Timestamp to a recognizable datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

    # Convert the datetime to a floating-point format that matplotlib can recognize
    df['date_num'] = matplotlib.dates.date2num(df['Timestamp'])

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

    return df  # Return the dataframe for later comparison

# Create a new figure with 1x2 subplots
fig = plt.figure(figsize=(20, 6))

ax1 = fig.add_subplot(121, projection='3d')
df1 = plot_3d_graph(ax1, rf"E:\Dissertation\combination\20230716_checkeddata\July3_2\force_data_2.csv")

ax2 = fig.add_subplot(122, projection='3d')
df2 = plot_3d_graph(ax2, rf"E:\Dissertation\combination\20230716_checkeddata\July3_1\force_data_8.csv")

# Find common scale
xlims = [min(df1['Fx'].min(), df2['Fx'].min()), max(df1['Fx'].max(), df2['Fx'].max())]
ylims = [min(df1['Fy'].min(), df2['Fy'].min()), max(df1['Fy'].max(), df2['Fy'].max())]
zlims = [min(df1['Fz'].min(), df2['Fz'].min()), max(df1['Fz'].max(), df2['Fz'].max())]

ax1.set_xlim(xlims)
ax1.set_ylim(ylims)
ax1.set_zlim(zlims)
ax2.set_xlim(xlims)
ax2.set_ylim(ylims)
ax2.set_zlim(zlims)

plt.tight_layout()  # Adjusts subplot params for better layout

ax1.text2D(0.05, 0.95, "Texture: Mesh", transform=ax1.transAxes)
ax2.text2D(0.05, 0.95, "Texture: Wool", transform=ax2.transAxes)
# Save the image and show it
image_path = "comparison_image.png"
plt.savefig(image_path)
plt.show()
