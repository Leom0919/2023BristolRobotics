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
fig, ax = plt.subplots(figsize=(18, 6))  # 设置图形窗口的大小

# 在figure上添加Fx和时间的关系图
ax.plot(df['date_num'], df['Fx'], label='Fx')
ax.xaxis_date()  # 将X轴转换为日期格式

# 设置坐标轴的标签和标题
ax.set_xlabel('Time')
ax.set_ylabel('Fx')
ax.set_title('Fx vs Time')

# 显示图例和图形
ax.legend()
plt.show()
