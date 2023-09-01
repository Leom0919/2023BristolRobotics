import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import os

# 创建文件名的列表
filenames = [rf"E:\Dissertation\Completedlc\June30_1\video_{i}DLC_resnet50_FingersJul22shuffle1_20000.csv" for i in range(1, 11)]

for idx, filename in enumerate(filenames):
    # 读取CSV文件
    data = pd.read_csv(filename, header=[0, 1, 2])

    x_coords = data['DLC_resnet50_FingersJul22shuffle1_20000', 'dot', 'x'].values
    y_coords = data['DLC_resnet50_FingersJul22shuffle1_20000', 'dot', 'y'].values

    # 假设图像的高度是h
    h = 360  # 你需要根据你的具体情况调整这个值
    y_coords = h - y_coords  # 翻转y坐标

    plt.figure(figsize=(10, 10))

    # 创建一个颜色图来指示点的顺序
    colors = np.arange(len(x_coords))

    # 检查是否在ROI内
    for i in range(len(x_coords)):
        if x_coords[i] >= 87 and x_coords[i] <= 387 and y_coords[i] >= 56 and y_coords[i] <= 356:  # Adjust the coordinates according to your ROI
            pass
        else:
            # 如果点超出了ROI，移动到边界上
            x_coords[i] = min(max(x_coords[i], 87), 387)  # Adjust the coordinates according to your ROI
            y_coords[i] = min(max(y_coords[i], 56), 356)  # Adjust the coordinates according to your ROI

    # 缩小点的大小
    scatter = plt.scatter(x_coords, y_coords, c=colors, cmap='viridis', s=20)

    # 为起点和终点添加特殊标记
    plt.scatter(x_coords[0], y_coords[0], color='red', label='Start', s=100)
    plt.scatter(x_coords[-1], y_coords[-1], color='blue', label='End', s=100)

    # 用颜色指示顺序，画出点之间的线
    for i in range(1, len(x_coords)):
        plt.plot(x_coords[i-1:i+1], y_coords[i-1:i+1], color=cm.viridis(colors[i]/len(x_coords)))

    plt.xlabel("X coordinates")
    plt.ylabel("Y coordinates")
    plt.title(f"Trajectory plot with order indicated by color for texture {idx+1}")

    # 假设数据以每秒12个点的速率采样
    # 为颜色条创建新的标签，以表示秒数
    colorbar = plt.colorbar(scatter)
    colorbar.set_label("Time (seconds)")
    new_labels = np.linspace(0, 10, num=11)  # 从0到10秒的标签
    colorbar.set_ticks(np.linspace(0, len(x_coords), num=11))  # 新标签的位置
    colorbar.set_ticklabels(new_labels)  # 设置新的标签

    plt.legend()  # 添加一个图例来解释颜色
    plt.grid()

    # 获取csv文件路径的目录
    dir_name = os.path.dirname(filename)
    # 构造图片保存路径
    output_filename = os.path.join(dir_name, f"trajectory_{idx + 1}.png")

    # 保存图像到指定的文件，每个文件的图像都不同
    plt.savefig(output_filename)

    plt.close()  # 关闭当前的图像窗口
