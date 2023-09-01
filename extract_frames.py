import cv2
vidcap = cv2.VideoCapture(r"E:\Dissertation\Completedlc\June30_1\\video_1.mp4"
                          )
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

# #获取视频高度和宽度
# import cv2
#
# # 打开视频文件
# cap = cv2.VideoCapture("C:\\Users\\dell\\Desktop\\Fingers-Ao-2023-07-22\\videos\\July3_3\\video_1DLC_resnet50_FingersJul22shuffle1_20000_labeled.mp4")
#
# # 获取视频帧的宽度和高度
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#
# print('Width: ', width)
# print('Height: ', height)