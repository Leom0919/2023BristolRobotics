import cv2

# 读取图像
img = cv2.imread('frame0.jpg')

# 在图像窗口中选择一个矩形区域
roi = cv2.selectROI(windowName='selectROI and press Enter', img=img, showCrosshair=True)

# roi 是一个四元组，包含了选择的矩形区域的 x, y, w, h
print(f'x: {roi[0]}, y: {roi[1]}, width: {roi[2]}, height: {roi[3]}')

# 销毁所有窗口
cv2.destroyAllWindows()
