import cv2
import numpy as np
import random
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import time
import forcesensor
import pandas as pd

def main():
    # 设置摄像头
    cap = cv2.VideoCapture(0);  # 设置摄像头端口
    width = int(cap.get(3))  # 在视频流的帧的宽度,3为编号，不能改
    height = int(cap.get(4))  # 在视频流的帧的高度,4为编号，不能改
    size = (width, height)
    fps = 30 # 帧率
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # 为视频编码方式，保存为mp4格式

    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)


    # 设置FTSensorSerial
    ft_sensor = forcesensor.FTSensorSerial()
    ft_sensor.set_zero_ref()

    # 使用tkinter获取输入的名字
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Welcome", "Welcome to our experiment!", parent=root)
    folder_name = simpledialog.askstring("Input", "请输入名字：", parent=root)

    if folder_name is None:
        root.destroy()
        return

    # 设置存储路径
    filepath = f"/home/leo/{folder_name}"  # 请替换为你的实际文件路径
    os.makedirs(filepath, exist_ok=True)

    used_numbers = []  # 已使用的随机数列表
    recording = False  # 标志位，用于指示是否开始录制
    start_time = None

    # 获取一个未使用过的随机数的函数
    def get_new_random():
        while True:
            new_random = random.randint(1, 10)
            if new_random not in used_numbers:
                used_numbers.append(new_random)
                return new_random

    random_number = get_new_random()

    print("按Enter键显示下一个随机数，按Q键停止录制。")
    force_data = []

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 1)  # 翻转

            if recording:
                # 显示录制时间
                elapsed_time = float(time.time() - start_time)
                cv2.putText(frame, f'Recorded: {elapsed_time} sec', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (128, 0, 0),
                            2)
                out.write(frame)  # 保存每一帧合并成视频

                # 读取力传感器数据
                force = ft_sensor.get_ft()
                force.append(time.time())  # 添加当前系统时间到力传感器数据中
                force_data.append(force)

                # 如果录制超过10秒，停止录制
                if elapsed_time >= 10:
                    recording = False
                    out.release()
                    # 将力传感器数据写入csv文件
                    force_data = np.array(force_data)
                    df = pd.DataFrame(force_data, columns=["Fx", "Fy", "Fz", "Tx", "Ty", "Tz", "Timestamp"])
                    csv_file = f"{filepath}/force_data_{random_number}.csv"
                    df.to_csv(csv_file, index=False)

                    force_data = []  # 清空力传感器数据列表以便于下一次录制

                    if len(used_numbers) < 10:  # 如果未使用完所有的随机数，获取一个新的随机数
                        random_number = get_new_random()
                    else:
                        break  # 已使用完所有的随机数，结束循环
            cv2.imshow('frame', frame)  # 显示视频界面

            # 创建一个空白图像并在其中添加随机数
            random_image = np.zeros((500, 500, 3), dtype='uint8')
            cv2.putText(random_image, f'Texture {random_number}', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2)
            cv2.imshow('random number', random_image)

            key = cv2.waitKey(1)
            if key == 13 and not recording:  # Enter 键的 ASCII 值为 13，开始录制
                recording = True
                start_time = time.time()  # 记录开始时间

                out = cv2.VideoWriter()
                out.open(f"{filepath}/video_{random_number}.mp4", fourcc, fps, size)
            elif key & 0xFF in [ord('Q'), ord('q')]:  # 按Q退出
                if recording:
                    recording = False
                    out.release()
                    # 将力传感器数据写入csv文件
                    force_data = np.array(force_data)
                    df = pd.DataFrame(force_data, columns=["Fx", "Fy", "Fz", "Tx", "Ty", "Tz", "Timestamp"])
                    csv_file = f"{filepath}/force_data_{random_number}.csv"
                    df.to_csv(csv_file, index=False)

                    force_data = []  # 清空力传感器数据列表以便于下一次录制

                    if len(used_numbers) < 10:  # 如果未使用完所有的随机数，获取一个新的随机数
                        random_number = get_new_random()
                    else:
                        break  # 已使用完所有的随机数，结束循环

        else:
            break

    # 完成所有操作后，释放摄像头和视频写入
    cap.release()
    cv2.destroyAllWindows()

    print("录制结束，数据已保存到以下位置：")
    print("视频文件: " + filepath + "/video_*.mp4")
    print("力传感器数据: " + filepath + "/force_data_*.csv")

if __name__ == "__main__":
    main()