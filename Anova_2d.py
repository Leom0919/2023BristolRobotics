import os
import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import glob
import statsmodels.api as sm
from statsmodels.formula.api import ols

base_dir = "E:\\Dissertation\\MyData"
subfolders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
video_path = rf"E:\Dissertation\MyData\July3_1\video_1.mp4"

texture_dict = {
    1: "Felt",
    2: "Mesh",
    3: "Nylon",
    4: "Acrylic",
    5: "Fashion Fabric",
    6: "Fur",
    7: "Canvas",
    8: "Wool",
    9: "Cotton",
    10: "Wood"
}


def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    plt.close()


cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise IOError("Cannot open video")

ret, frame = cap.read()

if not ret:
    raise IOError("Cannot read video frame")

fig, ax = plt.subplots()
ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

x_min = max(int(ix), 0)
y_min = max(int(iy), 0)
x_max = min(int(ix) + 300, frame.shape[1])
y_max = min(int(iy) + 300, frame.shape[0])

filenames = [os.path.join(base_dir, f"video_{i}DLC_resnet50_FingersJul22shuffle1_20000.csv") for i in range(1, 11)]


def compute_trajectory_length(x_coords, y_coords):
    length = 0
    for i in range(1, len(x_coords)):
        length += np.sqrt((x_coords[i] - x_coords[i - 1]) ** 2 + (y_coords[i] - y_coords[i - 1]) ** 2)
    return length


def get_metrics_from_file(filename, x_min, y_min, x_max, y_max):
    df = pd.read_csv(filename, header=[1, 2], index_col=0)
    df.columns = df.columns.droplevel()
    heatmap = np.zeros((y_max - y_min, x_max - x_min))
    x_coords = []
    y_coords = []

    for i in df.index:
        x = df.loc[i, 'x']
        y = df.loc[i, 'y']
        if x_min <= x <= x_max and y_min <= y <= y_max:
            heatmap[int(y) - y_min, int(x) - x_min] += 1
            x_coords.append(int(x) - x_min)
            y_coords.append(int(y) - y_min)

    heatmap = gaussian_filter(heatmap, sigma=10)
    threshold_value = 0
    binary_heatmap = (heatmap > threshold_value).astype(int)
    touch_area = np.sum(binary_heatmap)
    trajectory_length = compute_trajectory_length(x_coords, y_coords)

    return touch_area, trajectory_length


# Initialize lists of lists to store all values
touch_areas = [[] for _ in range(10)]
trajectory_lengths = [[] for _ in range(10)]
processed_files_count = 0


for subfolder in subfolders:
    for i in range(1, 11):
        filename = os.path.join(base_dir, subfolder, f"video_{i}_DLC.csv")
        if os.path.exists(filename):
            touch_area, trajectory_length = get_metrics_from_file(filename, x_min, y_min, x_max, y_max)
            touch_areas[i - 1].append(touch_area)
            trajectory_lengths[i - 1].append(trajectory_length)
            processed_files_count += 1
# Now, create a DataFrame for ANOVA
data = {
    'Texture': [],
    'TouchArea': [],
    'Trajectory_Length': []
}

for i in range(10):
    texture = texture_dict[i+1]
    for touch_area, traj_length in zip(touch_areas[i], trajectory_lengths[i]):
        data['Texture'].append(texture)
        data['TouchArea'].append(touch_area)
        data['Trajectory_Length'].append(traj_length)

df = pd.DataFrame(data)

# Perform ANOVA for TouchArea
model_touch = ols('TouchArea ~ C(Texture)', data=df).fit()
anova_table_touch = sm.stats.anova_lm(model_touch, typ=2)
print("ANOVA for Touch Area:")
print(anova_table_touch)

# Perform ANOVA for Trajectory_Length
model_traj = ols('Trajectory_Length ~ C(Texture)', data=df).fit()
anova_table_traj = sm.stats.anova_lm(model_traj, typ=2)
print("\nANOVA for Trajectory Length:")
print(anova_table_traj)


print(f"Total number of files processed: {processed_files_count}")