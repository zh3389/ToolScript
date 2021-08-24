import cv2 as cv

"""
环境搭建
pip install opencv-python==3.4.2.17
用于找出图像中特定对象的中心坐标
"""

image = cv.imread("1.jpg")
canny = cv.Canny(image, 200, 400)
# cv.imshow("canny", canny)
# cv.waitKey(0)
# exit()

_, contours, _ = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)


for i, contour in enumerate(contours):  # 所有轮廓
    if 10 < cv.contourArea(contour) <= 1000 and 0 < cv.arcLength(contour, True) < 2000:  # 指定外接矩形的面积和周长范围
        x, y, w, h = cv.boundingRect(contour)  # 外接矩形
        print(x, y, w, h, cv.contourArea(contour))
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv.imshow('image', image)
cv.waitKey(0)

