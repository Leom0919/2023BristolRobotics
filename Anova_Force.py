import os
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

# 定义文件路径和纹理字典
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

# 创建一个空的列表来存储结果
results = []

# 遍历所有文件夹和文件
for folder in os.listdir(base_path):
    for i in range(1, 11):  # 从1到10遍历
        file_path = os.path.join(base_path, folder, f'force_data_{i}.csv')
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)

            # 修改数据添加方式
            for value in df['Fz']:
                results.append({'Fz': value, 'texture': texture_dict[i]})

# 将结果列表转为DataFrame
results_df = pd.DataFrame(results)

# Conduct ANOVA
model = ols('Fz ~ C(texture)', data=results_df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# Tukey HSD test for post-hoc analysis
mc = MultiComparison(results_df['Fz'], results_df['texture'])
result = mc.tukeyhsd()
print(result)
