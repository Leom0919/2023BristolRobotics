import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 从您提供的输出结果创建DataFrame
data = {
    'Textures': ['Felt', 'Mesh', 'Nylon', 'Acrylic', 'Fashion Fabric', 'Fur', 'Canvas', 'Wool', 'Cotton', 'Wood'],
    'Average Fz (N)': [-0.765225, -0.838471, -0.851784, -0.647896, -0.786572, -0.567382, -0.978833, -0.979005, -0.835818, -0.887785],
    'Q1': [-0.949812, -1.004438, -1.030563, -0.823563, -0.961250, -0.671312, -1.217062, -1.191812, -1.018000, -1.157437],
    'Q3': [-0.484375, -0.511937, -0.558063, -0.363437, -0.475500, -0.316063, -0.616812, -0.606437, -0.531500, -0.504000]
}
df = pd.DataFrame(data)

# 计算IQR (四分位距)和whiskers
IQR = df['Q3'] - df['Q1']
lower_whisker = df['Q1'] - 1.5 * IQR
upper_whisker = df['Q3'] + 1.5 * IQR

plt.figure(figsize=(12, 8))
# 使用bar表示均值
plt.bar(df['Textures'], df['Average Fz (N)'], color='skyblue', align='center')
# 使用errorbar表示箱线图的特点
for i, texture in enumerate(df['Textures']):
    plt.errorbar(x=i, y=df['Average Fz (N)'].iloc[i], yerr=[[df['Average Fz (N)'].iloc[i] - lower_whisker.iloc[i]], [upper_whisker.iloc[i] - df['Average Fz (N)'].iloc[i]]], color='black', capsize=5)

plt.ylabel('Average Fz (N)')
plt.title("Vertical force for various textures")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
