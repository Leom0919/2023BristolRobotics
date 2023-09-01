import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# 读取CSV文件
df = pd.read_csv('../test_data/test_1/force_data_1.csv')

# 创建一个网格数据
xi = np.linspace(df['Fx'].min(), df['Fx'].max(), 100)
yi = np.linspace(df['Fy'].min(), df['Fy'].max(), 100)
zi = griddata((df['Fx'], df['Fy']), df['Fz'], (xi[None,:], yi[:,None]), method='cubic')

# 创建一个新的figure
fig = plt.figure()

# 在figure上添加一个3D subplot
ax = fig.add_subplot(111, projection='3d')

# 在3D图上绘制数据
X, Y = np.meshgrid(xi, yi)
ax.plot_surface(X, Y, zi, cmap='viridis')

# 设置坐标轴的标签
ax.set_xlabel('Fx')
ax.set_ylabel('Fy')
ax.set_zlabel('Fz')

# 显示图形
plt.show()
