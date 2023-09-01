import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# 这两个变量的数据（需要替换为实际数据）
roughness = np.array([2.5, -2, 3, -8, 2, 0.5, 4, 6, 3, -0.5])  #  'Roughness' 数据
median_force = np.array([0.63,0.61,0.74,0.49,0.59,0.43,0.79,0.77,0.67,0.7])  #  'Median Force' 数据

# 使用 scipy's linregress 来获取回归线的参数
slope, intercept, r_value, p_value, std_err = linregress(roughness, median_force)

# 计算 R^2 值
r_squared = r_value**2

# 创建一个图形
plt.figure(figsize=(10, 6))

# 使用 seaborn 来绘制回归线
sns.regplot(x=roughness, y=median_force, color="blue", line_kws={'label': f"y = {slope:.2f}x + {intercept:.2f}, $R^2$ = {r_squared:.2f}"})

# 添加标签和标题
plt.title("Linear Regression between 'Roughness' and 'Median Force'")
plt.xlabel('Roughness')
plt.ylabel('Median Force')
plt.legend()

# 显示图形
plt.show()
