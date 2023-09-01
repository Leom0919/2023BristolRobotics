import pandas as pd

# 使用您提供的数据创建一个DataFrame
data = {
    'group1': ['Acrylic', 'Acrylic', 'Acrylic', 'Acrylic', 'Acrylic', 'Acrylic', 'Acrylic', 'Acrylic', 'Acrylic',
               'Canvas', 'Canvas', 'Canvas', 'Canvas', 'Canvas', 'Canvas', 'Canvas', 'Canvas', 'Cotton',
               'Cotton', 'Cotton', 'Cotton', 'Cotton', 'Cotton', 'Cotton', 'Fashion Fabric', 'Fashion Fabric',
               'Fashion Fabric', 'Fashion Fabric', 'Fashion Fabric', 'Fashion Fabric', 'Felt', 'Felt', 'Felt',
               'Felt', 'Felt', 'Fur', 'Fur', 'Fur', 'Fur', 'Mesh', 'Mesh', 'Mesh', 'Nylon', 'Nylon', 'Wood'],

    'group2': ['Canvas', 'Cotton', 'Fashion Fabric', 'Felt', 'Fur', 'Mesh', 'Nylon', 'Wood', 'Wool', 'Cotton',
               'Fashion Fabric', 'Felt', 'Fur', 'Mesh', 'Nylon', 'Wood', 'Wool', 'Fashion Fabric', 'Felt', 'Fur',
               'Mesh', 'Nylon', 'Wood', 'Wool', 'Felt', 'Fur', 'Mesh', 'Nylon', 'Wood', 'Wool', 'Fur', 'Mesh',
               'Nylon', 'Wood', 'Wool', 'Mesh', 'Nylon', 'Wood', 'Wool', 'Nylon', 'Wood', 'Wool', 'Wood', 'Wool',
               'Wool'],

    'p-adj': [0.0, 0.0, 0.0, 0.0, 0.0093, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0018, 1.0, 0.5641, 0.0377,
              0.0, 1.0, 0.9996, 0.282, 0.0, 0.9719, 0.0, 0.408, 0.1651, 0.0003, 0.0, 0.0, 0.0182, 0.0035, 0.0, 0.0, 0.0,
              0.0, 0.0, 0.0, 1.0, 0.4228, 0.0, 0.7426, 0.0, 0.0025]
}

df = pd.DataFrame(data)

# 对每个纹理计算平均p值
avg_p_values = df.groupby('group1')['p-adj'].mean()

print(avg_p_values)
