import os
import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter
import cv2
import matplotlib.pyplot as plt
from matplotlib import cm
import glob

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

filenames = [os.path.join(base_dir, f"video_{i}DLC.csv") for i in range(1, 11)]

def compute_trajectory_length(x_coords, y_coords):
    length = 0
    for i in range(1, len(x_coords)):
        length += np.sqrt((x_coords[i] - x_coords[i-1])**2 + (y_coords[i] - y_coords[i-1])**2)
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

touch_area_sums = np.zeros(10)
trajectory_length_sums = np.zeros(10)
count_files = np.zeros(10)
all_touch_areas = [list() for _ in range(10)]
all_trajectory_lengths = [list() for _ in range(10)]

for subfolder in subfolders:
    for i in range(1, 11):
        matching_files = glob.glob(os.path.join(base_dir, subfolder, f"video_{i}_DLC.csv"))

        for filename in matching_files:

            touch_area, trajectory_length = get_metrics_from_file(filename, x_min, y_min, x_max, y_max)

            # 将每个文件的触摸面积和轨迹长度追加到相应的列表中。
            all_touch_areas[i - 1].append(touch_area)
            all_trajectory_lengths[i - 1].append(trajectory_length)

            touch_area_sums[i - 1] += touch_area
            trajectory_length_sums[i - 1] += trajectory_length
            count_files[i - 1] += 1

touch_area_averages = touch_area_sums / count_files
trajectory_length_averages = trajectory_length_sums / count_files
# 计算方差
touch_area_variances = [np.var(touch_areas) for touch_areas in all_touch_areas]
trajectory_length_variances = [np.var(trajectory_lengths) for trajectory_lengths in all_trajectory_lengths]

print("Average Touch Areas for each texture:", touch_area_averages)
print("Average Trajectory Lengths for each texture:", trajectory_length_averages)
# 计算标准偏差
touch_area_std_devs = [np.sqrt(variance) for variance in touch_area_variances]
trajectory_length_std_devs = [np.sqrt(variance) for variance in trajectory_length_variances]

print("Standard Deviation of Touch Areas for each texture:", touch_area_std_devs)
print("Standard Deviation of Trajectory Lengths for each texture:", trajectory_length_std_devs)

total_files_processed = int(sum(count_files))
print(f"Total number of files processed: {total_files_processed}")