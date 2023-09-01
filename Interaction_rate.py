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
# ... [省略的代码没有改变]

all_touch_areas = [list() for _ in range(10)]
all_trajectory_lengths = [list() for _ in range(10)]

for subfolder in subfolders:
    for i in range(1, 11):
        matching_files = glob.glob(os.path.join(base_dir, subfolder, f"video_{i}_DLC.csv"))

        for filename in matching_files:
            touch_area, trajectory_length = get_metrics_from_file(filename, x_min, y_min, x_max, y_max)
            all_touch_areas[i - 1].append(touch_area)
            all_trajectory_lengths[i - 1].append(trajectory_length)
            touch_area_sums[i - 1] += touch_area
            trajectory_length_sums[i - 1] += trajectory_length
            count_files[i - 1] += 1

# 这里定义了 touch_area_averages
touch_area_averages = touch_area_sums / count_files

# 计算交互率
interaction_rates = (touch_area_averages / 90000) * 100

# 计算标准偏差
touch_area_variances = [np.var(touch_areas) for touch_areas in all_touch_areas]
touch_area_std_devs = [np.sqrt(variance) for variance in touch_area_variances]

# 计算标准误
touch_area_std_errors = [std_dev / np.sqrt(count) for std_dev, count in zip(touch_area_std_devs, count_files)]

print("Interaction Rates for each texture:", interaction_rates)
print("Standard Errors of Touch Areas for each texture:", touch_area_std_errors)


# # 整合每个纹理的数据
# texture_data = {}
# for idx, texture_name in texture_dict.items():
#     texture_data[texture_name] = {
#         'Interaction Rate': interaction_rates[idx - 1],
#         'Standard Error': touch_area_std_errors[idx - 1]
#     }
#
# print(texture_data)
# 转化为百分比的标准误
percentage_standard_errors = [(std_error / 90000) * 100 for std_error in touch_area_std_devs]

print("Interaction Rates for each texture:", touch_area_averages / 900)
print("Standard Errors of Interaction Rates for each texture (in %):", percentage_standard_errors)
