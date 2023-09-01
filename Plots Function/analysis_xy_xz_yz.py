import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# 读取CSV文件
df = pd.read_csv('../test_data/test_1/force_data_1.csv')

# 创建一个新的figure
fig = plt.figure(figsize=(18, 6))  # 设置图形窗口的大小

# 在figure上添加第一个3D subplot
ax1 = fig.add_subplot(131, projection='3d')  # 这里的131表示1行3列的第1个图

# 创建网格数据
xi = np.linspace(df['Fx'].min(), df['Fx'].max(), 100)
yi = np.linspace(df['Fy'].min(), df['Fy'].max(), 100)
zi = griddata((df['Fx'], df['Fy']), df['Fz'], (xi[None,:], yi[:,None]), method='cubic')

# 在3D图上绘制数据
X, Y = np.meshgrid(xi, yi)
ax1.plot_surface(X, Y, zi, cmap='viridis')

# 设置坐标轴的标签
ax1.set_xlabel('Fx')
ax1.set_ylabel('Fy')
ax1.set_zlabel('Fz')

# 在figure上添加第二个3D subplot
ax2 = fig.add_subplot(132, projection='3d')  # 这里的132表示1行3列的第2个图

# 创建网格数据
xi = np.linspace(df['Fz'].min(), df['Fz'].max(), 100)
yi = np.linspace(df['Fx'].min(), df['Fx'].max(), 100)
zi = griddata((df['Fz'], df['Fx']), df['Fy'], (xi[None,:], yi[:,None]), method='cubic')

# 在3D图上绘制数据
X, Y = np.meshgrid(xi, yi)
ax2.plot_surface(X, Y, zi, cmap='viridis')

# 设置坐标轴的标签
ax2.set_xlabel('Fz')
ax2.set_ylabel('Fx')
ax2.set_zlabel('Fy')

# 在figure上添加第三个3D subplot
ax3 = fig.add_subplot(133, projection='3d')  # 这里的133表示1行3列的第3个图

# 创建网格数据
xi = np.linspace(df['Fy'].min(), df['Fy'].max(), 100)
yi = np.linspace(df['Fz'].min(), df['Fz'].max(), 100)
zi = griddata((df['Fy'], df['Fz']), df['Fx'], (xi[None,:], yi[:,None]), method='cubic')

# 在3D图上绘制数据
X, Y = np.meshgrid(xi, yi)
ax3.plot_surface(X, Y, zi, cmap='viridis')

# 设置坐标轴的标签
ax3.set_xlabel('Fy')
ax3.set_ylabel('Fz')
ax3.set_zlabel('Fx')

# 显示图形
plt.show(block=True)
