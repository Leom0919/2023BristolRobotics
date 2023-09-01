import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
import os

# 数据文件的根目录
root_directory = "E:/Dissertation/combination/20230716_checkeddata/"

# 使用 os.walk 遍历所有子目录
for directory, subdirs, files in os.walk(root_directory):
    # 检查当前目录下是否有符合要求的文件
    for file in files:
        if file.startswith("force_data_") and file.endswith(".csv"):
            # 构造完整的文件路径
            file_path = os.path.join(directory, file)

            # 读取CSV文件
            df = pd.read_csv(file_path)

            # 将Timestamp转换为可识别的日期时间格式
            df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

            # 将日期时间转换为matplotlib可以识别的浮点格式
            df['date_num'] = matplotlib.dates.date2num(df['Timestamp'])

            # 创建一个新的figure
            fig, ax = plt.subplots(figsize=(18, 6))  # 设置图形窗口的大小

            # 在figure上添加Fz和时间的关系图
            ax.plot(df['date_num'], df['Fz'], label='Fz', color='g')
            ax.xaxis_date()  # 将X轴转换为日期格式

            # 计算 Fz 的平均值、最小值和最大值
            avg_fz = df['Fz'].mean()
            min_fz = df['Fz'].min()
            max_fz = df['Fz'].max()

            # 在图中添加平均值、最小值和最大值的文本
            ax.text(0.01, 0.95, f"Average Fz: {avg_fz:.2f}", transform=ax.transAxes)
            ax.text(0.01, 0.90, f"Min Fz: {min_fz:.2f}", transform=ax.transAxes)
            ax.text(0.01, 0.85, f"Max Fz: {max_fz:.2f}", transform=ax.transAxes)

            # 设置坐标轴的标签和标题
            ax.set_xlabel('Time')
            ax.set_ylabel('Fz')
            ax.set_title(f'Fz vs Time for {file}') # 设置每个图的标题

            # 显示图例
            ax.legend()

            # 保存图形至当前路径
            output_file_path = os.path.join(directory, f'Fz_vs_Time_for_{os.path.splitext(file)[0]}.png')  # PNG格式
            plt.savefig(output_file_path)

            # 关闭图形
            plt.close(fig)
