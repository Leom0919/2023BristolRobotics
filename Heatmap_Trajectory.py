import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter
import cv2
import os
from matplotlib import cm

base_dir = "E:\\Dissertation\\Completedlc\\July3_1"  # 设置基础目录
video_path = os.path.join(base_dir, "video_1.mp4")  # 生成视频文件路径
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

cap = cv2.VideoCapture(video_path)  # 使用生成的视频路径

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

filenames = [os.path.join(base_dir, f"video_{i}DLC_resnet50_FingersJul22shuffle1_20000.csv") for i in range(1, 11)]  # 使用基础目录生成csv文件路径

blur_radius = 10

for idx, filename in enumerate(filenames):
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

    heatmap = gaussian_filter(heatmap, sigma=blur_radius)

    # 翻转 y 轴
    y_coords = [y_max - y_min - coord for coord in y_coords]

    # Use [::-1] to flip the heatmap upside down before plotting.
    plt.imshow(heatmap[::-1], cmap='jet', interpolation='nearest')

    # 添加一个 'X' 标记在同一位置
    start_cross = plt.scatter(x_coords[0], y_coords[0], color='black', marker='x', s=200)
    # 创建图例
    plt.legend([start_cross], ['Start Point'], loc='upper right', bbox_to_anchor=(1, 1), borderaxespad=0., scatterpoints=1, handletextpad=0, markerscale=1)
    plt.xlim(0, x_max - x_min)
    plt.ylim(0, y_max - y_min)
    dir_name = os.path.dirname(filename)
    heatmap_filename = os.path.join(dir_name, f"heatmap_{idx + 1}.png")
    plt.savefig(heatmap_filename)
    plt.close()
    #Plot
    colors = np.arange(len(x_coords))

    scatter = plt.scatter(x_coords, y_coords, c=colors, cmap='viridis', s=20)
    plt.scatter(x_coords[0], y_coords[0], color='red', label='Start', s=100)
    plt.scatter(x_coords[-1], y_coords[-1], color='blue', label='End', s=100)
    plt.xlim(0, x_max - x_min)
    plt.ylim(0, y_max - y_min)

    for i in range(1, len(x_coords)):
        plt.plot(x_coords[i - 1:i + 1], y_coords[i - 1:i + 1], color=cm.viridis(colors[i] / len(x_coords)))

    colorbar = plt.colorbar(scatter)
    colorbar.set_label("Time (seconds)")
    new_labels = np.linspace(0, 10, num=11)
    colorbar.set_ticks(np.linspace(0, len(x_coords), num=11))
    colorbar.set_ticklabels(new_labels)

    plt.legend()
    plt.grid()

    # Add title to the plot
    plt.title(f"Trajectory plot with time indicated by color for {texture_dict[idx + 1]}")

    trajectory_filename = os.path.join(dir_name, f"trajectory_{idx + 1}.png")

    plt.savefig(trajectory_filename)

    plt.close()
