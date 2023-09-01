import os
import glob

base_dir = "E:\\Dissertation\\MyData"
subfolders = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

for subfolder in subfolders:
    matching_files = glob.glob(os.path.join(subfolder, "video_*DLC_resnet50*.csv"))
    for filename in matching_files:
        # 提取视频编号，例如从"video_4DLC_resnet50_FingersJul22shuffle1_20000.csv"中提取"4"
        video_number = filename.split("video_")[1].split("DLC")[0]
        # 创建新的文件名
        new_name = f"video_{video_number}_DLC.csv"
        new_path = os.path.join(subfolder, new_name)
        os.rename(filename, new_path)
        print(f"Renamed {filename} to {new_path}")
