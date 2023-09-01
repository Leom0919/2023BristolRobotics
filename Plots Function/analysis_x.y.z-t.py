import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates

# 读取CSV文件
df = pd.read_csv('../test_data/test_2_only3/force_data_7.csv')

# 将Timestamp转换为可识别的日期时间格式
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

# 将日期时间转换为matplotlib可以识别的浮点格式
df['date_num'] = matplotlib.dates.date2num(df['Timestamp'])

# 创建一个新的figure
fig, ax = plt.subplots(3, 1, figsize=(18, 18))  # 设置图形窗口的大小

# 在figure上添加Fx和时间的关系图
ax[0].plot(df['date_num'], df['Fx'], label='Fx')
ax[0].xaxis_date()  # 将X轴转换为日期格式

# 设置坐标轴的标签和标题
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Fx')
# ax[0].set_title('Fx vs Time')

# 显示图例
ax[0].legend()

# 在figure上添加Fy和时间的关系图
ax[1].plot(df['date_num'], df['Fy'], label='Fy', color='r')
ax[1].xaxis_date()  # 将X轴转换为日期格式

# 设置坐标轴的标签和标题
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Fy')
# ax[1].set_title('Fy vs Time')

# 显示图例
ax[1].legend()

# 在figure上添加Fz和时间的关系图
ax[2].plot(df['date_num'], df['Fz'], label='Fz', color='g')
ax[2].xaxis_date()  # 将X轴转换为日期格式

# 设置坐标轴的标签和标题
ax[2].set_xlabel('Time')
ax[2].set_ylabel('Fz')
# ax[2].set_title('Fz vs Time')

# 显示图例
ax[2].legend()

# 显示图形
plt.tight_layout()  # 自动调整子图间的空白
plt.show()
