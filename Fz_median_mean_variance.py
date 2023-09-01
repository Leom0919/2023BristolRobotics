import os
import pandas as pd

# 定义文件路径
base_path = "E:\\Dissertation\\combination\\20230716_checkeddata"
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

# 创建一个空的DataFrame来存储结果
results_list = []

# 遍历所有文件夹和文件
for folder in os.listdir(base_path):
    for i in range(1, 11):  # 从1到10遍历
        file_path = os.path.join(base_path, folder, f'force_data_{i}.csv')
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)

            # 只取Fz这个列的平均值
            avg = {'Fz': df['Fz'].mean(), 'texture': texture_dict[i]}

            results_list.append(avg)

# 将结果列表组合成一个DataFrame
results = pd.DataFrame(results_list)

# 按纹理(texture)分组，取平均值，并重置索引
average_results = results.groupby('texture').mean().reset_index()

# 使用reindex方法按照texture_dict的顺序来重新排序
texture_order = ["Felt", "Mesh", "Nylon", "Acrylic", "Fashion Fabric", "Fur", "Canvas", "Wool", "Cotton", "Wood"]
average_results_ordered = average_results.set_index('texture').reindex(texture_order).reset_index()

# 打印结果
print(average_results_ordered)

#
# import os
# import pandas as pd
#
# # 定义文件路径
# base_path = "E:\\Dissertation\\combination\\20230716_checkeddata"
# texture_dict = {
#     1: "Felt",
#     2: "Mesh",
#     3: "Nylon",
#     4: "Acrylic",
#     5: "Fashion Fabric",
#     6: "Fur",
#     7: "Canvas",
#     8: "Wool",
#     9: "Cotton",
#     10: "Wood"
# }
#
# # 创建一个空的DataFrame来存储结果
# results_list = []
#
# # 遍历所有文件夹和文件
# for folder in os.listdir(base_path):
#     for i in range(1, 11):  # 从1到10遍历
#         file_path = os.path.join(base_path, folder, f'force_data_{i}.csv')
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)
#
#             # 将每个文件的Fz列添加到结果列表中
#             median_data = {'Fz': df['Fz'].tolist(), 'texture': texture_dict[i]}
#             results_list.append(median_data)
#
# # 将结果列表组合成一个DataFrame
# results = pd.DataFrame(results_list)
#
# # 展开Fz列，使每个值都有一个单独的行
# results = results.explode('Fz')
#
# # 按纹理(texture)分组，取中位数，并重置索引
# median_results = results.groupby('texture').median().reset_index()
#
# # 使用reindex方法按照texture_dict的顺序来重新排序
# texture_order = ["Felt", "Mesh", "Nylon", "Acrylic", "Fashion Fabric", "Fur", "Canvas", "Wool", "Cotton", "Wood"]
# median_results_ordered = median_results.set_index('texture').reindex(texture_order).reset_index()
#
# # 打印结果
# print(median_results_ordered)
#
import os
import pandas as pd

# # 定义文件路径
# base_path = "E:\\Dissertation\\combination\\20230716_checkeddata"
# texture_dict = {
#     1: "Felt",
#     2: "Mesh",
#     3: "Nylon",
#     4: "Acrylic",
#     5: "Fashion Fabric",
#     6: "Fur",
#     7: "Canvas",
#     8: "Wool",
#     9: "Cotton",
#     10: "Wood"
# }
#
# # 创建一个空的DataFrame来存储结果
# results_list = []
#
# # 遍历所有文件夹和文件
# for folder in os.listdir(base_path):
#     for i in range(1, 11):  # 从1到10遍历
#         file_path = os.path.join(base_path, folder, f'force_data_{i}.csv')
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)
#
#             # 将每个文件的Fz列添加到结果列表中
#             variance_data = {'Fz': df['Fz'].tolist(), 'texture': texture_dict[i]}
#             results_list.append(variance_data)
#
# # 将结果列表组合成一个DataFrame
# results = pd.DataFrame(results_list)
#
# # 展开Fz列，使每个值都有一个单独的行
# results = results.explode('Fz')
#
# # 按纹理(texture)分组，计算方差，并重置索引
# variance_results = results.groupby('texture').var().reset_index()
#
# # 使用reindex方法按照texture_dict的顺序来重新排序
# texture_order = ["Felt", "Mesh", "Nylon", "Acrylic", "Fashion Fabric", "Fur", "Canvas", "Wool", "Cotton", "Wood"]
# variance_results_ordered = variance_results.set_index('texture').reindex(texture_order).reset_index()
#
# # 打印结果
# print(variance_results_ordered)
