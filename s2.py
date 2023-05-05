# import cv2

# img = cv2.imread("D:\soft\python\python_project\lenet\data\WN6CW29.jpg")
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# adaptive_thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 333, 1)
# cv2.imshow("g",gray_img)
# cv2.waitKey(0)
# cv2.imshow("1",adaptive_thresh)
# cv2.waitKey(0)

# def split_img(img):
#     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     adaptive_thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 333, 1)

import numpy as np

# 创建一个3x3的矩阵
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# 返回所有大于5的元素的索引
indices = np.where(arr > 5)
print(indices[1,2,2,2])  # 输出：(array([1, 2, 2, 2]), array([2, 0, 1, 2]))

# 返回所有大于5的元素
values = np.where(arr > 5, arr, 0)
print(values)  # 输出：array([[0, 0, 0], [0, 0, 6], [7, 8, 9]])
