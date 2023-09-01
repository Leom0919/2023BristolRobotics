import pandas as pd
import matplotlib.pyplot as plt

# 定义纹理字典
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

# 选择要加载的列（第二列到第四十一列）
cols = list(range(1, 41))

# 设置权重
weights = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}

# 通过一个循环读取数据并绘制饼图
for i in range(0, 50, 5):
    # 读取CSV文件，每次跳过i行，并只读取5行
    df = pd.read_csv(r"E:\Dissertation\饼图.csv", index_col=0, usecols=cols, skiprows=range(1, i), nrows=5)

    # 使用字典替换每个值并计算每行的权重和
    df_weighted = df.replace(weights).fillna(0).sum(axis=1)

    # 创建饼图
    plt.figure(i // 5)  # 创建一个新的图形
    labels = ["Traction", "Roughness", "Fineness", "Hardness", "Temperature"]
    plt.pie(df_weighted, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')  # 使饼图为正圆形

    # 使用texture_dict设置图形标题
    plt.title(f'Texture {texture_dict[1 + i // 5]}')  # 设置图形标题

    plt.show()  # 显示图像
