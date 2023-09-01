import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.ndimage import gaussian_filter

# 创建文件名的列表
filenames = [
    f"E:\\Dissertation\\Completedlc\June30_1\\video_{i}DLC_resnet50_FingersJul22shuffle1_20000.csv"
    for i in range(1, 11)]

# 视频宽度和高度
w, h = 640, 360

# Gaussian blur radius
blur_radius = 10
# 跳跃阈值
jump_threshold = 40

def crop_heatmap(heatmap):
    # 找到heatmap中非零元素的坐标
    coords = np.argwhere(heatmap)

    # 找到这些坐标的边界
    x_min, y_min = (0,0) #coords.min(axis=0) # TODO: FIX VALUE
    x_max, y_max = (360,360) #coords.max(axis=0)

    # 生成切片索引
    return np.s_[x_min:x_max+1, y_min:y_max+1]

for idx, filename in enumerate(filenames):
    # 读取CSV文件
    data = pd.read_csv(filename, header=[0, 1, 2])

    x_coords = data['DLC_resnet50_FingersJul22shuffle1_20000', 'dot', 'x'].values
    y_coords = h - data['DLC_resnet50_FingersJul22shuffle1_20000', 'dot', 'y'].values  # 翻转y坐标

    # 创建一个空的热图
    heatmap = np.zeros((h, w))

    # 初始化前一个点的坐标
    prev_x, prev_y = x_coords[0], y_coords[0]

    # 在观察到的点周围增加值
    for x, y in zip(x_coords.astype(int), y_coords.astype(int)):
        # 计算与前一个点的距离
        distance = np.sqrt((x - prev_x)**2 + (y - prev_y)**2)

        # 只有当距离小于阈值时才增加值
        if distance < jump_threshold:
            # 检查是否在ROI内
            if x >= 87 and x <= 387 and y >= 56 and y <= 356:  # Adjust the coordinates according to your ROI
                heatmap[y, x] += 1
            else:
                # 如果点超出了ROI，移动到边界上
                x = min(max(x, 87), 387)  # Adjust the coordinates according to your ROI
                y = min(max(y, 56), 356)  # Adjust the coordinates according to your ROI
                heatmap[y, x] += 1

        # 更新前一个点的坐标
        prev_x, prev_y = x, y

    # 对热图进行高斯模糊，以模拟点的扩散
    heatmap = gaussian_filter(heatmap, sigma=blur_radius)

    # 计算热图的切片索引
    heatmap_slice = crop_heatmap(heatmap)

    # 用imshow绘制热图，使用jet颜色方案
    plt.figure(figsize=(10, 10))
    plt.imshow(heatmap[heatmap_slice], origin='lower', cmap='jet')

    # 添加一个 'X' 标记在同一位置
    start_cross = plt.scatter(x_coords[0]-heatmap_slice[1].start, y_coords[0]-heatmap_slice[0].start, color='black', marker='x', s=200)

    # 创建图例
    plt.legend([start_cross], [ 'Start Point'], loc='upper right', bbox_to_anchor=(1, 1), borderaxespad=0., scatterpoints=1, handletextpad=0, markerscale=1)

    plt.colorbar(label='Frequency')
    plt.title(f"Touch heatmap for texture {idx + 1}")

    # 获取csv文件路径的目录
    dir_name = os.path.dirname(filename)
    # 构造图片保存路径
    output_filename = os.path.join(dir_name, f"heatmap_{idx + 1}.png")

    # 保存图像到指定的文件，每个文件的图像都不同
    plt.savefig(output_filename)

    plt.close()  # 关闭当前的图像窗口
