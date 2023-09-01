import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
# 假设你已经有了这两个变量的数据

trajectory_length = np.array([17.410, 17.733, 17.447, 15.000, 17.208,
                              22.859, 16.748, 16.007, 17.111, 15.228])  # 请替换为实际的 'Trajectory Length' 数据
hardness = np.array([-6, 6, 5, 7, -1.5, -8, 5, -4, 0.5, 5])  # 请替换为实际的 'Hardness' 数据

# 获取回归线的参数
slope, intercept, r_value, p_value, std_err = linregress(hardness, trajectory_length)

# 计算 R^2 值
r_squared = r_value**2

# 绘制回归线
plt.figure(figsize=(10, 6))
sns.regplot(x=hardness, y=trajectory_length, color="blue", line_kws={'label': f"y = {slope:.2f}x + {intercept:.2f}, $R^2$ = {r_squared:.2f}"})

# 添加标签和标题
plt.title("Linear Regression between 'Hardness' and 'Trajectory Length'")
plt.xlabel('Hardness')
plt.ylabel('Trajectory Length (x $10^2$)')
plt.legend()

plt.show()
