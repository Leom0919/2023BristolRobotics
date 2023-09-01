import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# 假设你已经有了这两个变量的数据
touch_area = np.array([30.2910, 30.3991, 30.6004, 29.8116, 30.7124, 34.7645, 28.7475, 30.7335, 29.2751, 29.2061])  # 请替换为实际的 'Touch Area' 数据
hardness = np.array([-6, 6, 5, 7, -1.5, -8, 5, -4, 0.5, 5])  # 请替换为实际的 'Hardness' 数据

# 获取回归线的参数
slope, intercept, r_value, p_value, std_err = linregress(hardness, touch_area)

# 计算 R^2 值
r_squared = r_value**2

# 绘制回归线
plt.figure(figsize=(10, 6))
sns.regplot(x=hardness, y=touch_area, color="blue", line_kws={'label': f"y = {slope:.2f}x + {intercept:.2f}, $R^2$ = {r_squared:.2f}"})

# 添加标签和标题
plt.title("Linear Regression between 'Hardness' and 'Touch Area'")
plt.xlabel('Hardness')
plt.ylabel('Touch Area (x $10^3$)')
plt.legend()

plt.show()
