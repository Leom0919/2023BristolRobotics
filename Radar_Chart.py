import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取excel文件
excel_data = pd.read_excel(r"E:\Dissertation\雷达图.xlsx", header=None)

# 选择需要的列（从第三列(C)到第42列(AP)，列索引从0开始计数）
excel_data = excel_data.iloc[:, 2:42]

data = {}
q25 = {}
q75 = {}

labels = ["Traction", "Roughness", "Fineness", "Hardness", "Temperature"]
for i, label in enumerate(labels):
    data_row = excel_data.iloc[i+45, :] # 自加5 from figure1-figure10
    data[label] = data_row.median()
    q25[label] = data_row.quantile(0.25)
    q75[label] = data_row.quantile(0.75)

# 调整数据到新的区间
for key in data:
    data[key] = 10 + data[key]  # 将区间从[-10, 10]变换到[0, 20]
    q25[key] = 10 + q25[key]
    q75[key] = 10 + q75[key]

labels = np.array(list(data.keys()))
stats = np.array(list(data.values()))
q25 = np.array(list(q25.values()))
q75 = np.array(list(q75.values()))

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

stats = np.concatenate((stats, [stats[0]]))
q25 = np.concatenate((q25, [q25[0]]))
q75 = np.concatenate((q75, [q75[0]]))
angles_closed = np.concatenate((angles, [angles[0]]))

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Fill areas
ax.fill(angles_closed, q75, color='#FF0000', alpha=0.2)  # outer layer (75% quantile, light red)
ax.fill(angles_closed, stats, color='#FF0000', alpha=0)  # middle layer (median, red)
ax.fill(angles_closed, q25, color='white', alpha=1.0)  # inner layer (25% quantile, dark red)

# Connect Q75 points with a thick line
ax.plot(angles_closed, stats, color='red', linewidth=2, alpha=1)

# Add median points
ax.scatter(angles_closed, stats, color='purple', s=30)  # median points

####### Comment Display median values on the chart
for angle, value, label in zip(angles_closed, stats, labels):
    ax.text(angle, value + 1, f"{value-10:.2f}", ha='center', va='bottom', color='black')  # value-10 to adjust for the new range

# Set the range and labels of the radar chart
ax.set_ylim(0, 20)  # Range from 0 to 20
ax.set_yticks([0, 5, 10, 15, 20])  # Set y-axis ticks
ax.set_yticklabels(['-10', '-5', '0', '5', '10'])  # Set y-axis tick labels
ax.set_rgrids([0, 5, 10, 15, 20], angle=20, fontsize=10)
ax.spines['polar'].set_visible(False)
ax.set_thetagrids(np.degrees(angles), labels, fontweight='bold', fontsize=12)
ax.xaxis.grid(color='gray', linestyle='solid', linewidth=0.5)
ax.yaxis.grid(color='gray', linestyle='solid', linewidth=0.5)

plt.show()
