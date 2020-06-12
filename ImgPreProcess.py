import tensorflow as tf
import cv2 as cv
import numpy as np
image = cv.imread("G:/Code/python/faceRecognition/photos/wwl/0.jpg")
cv.imshow("input", image)
cv.waitKey(0)
print(image)
'''
图像标准化
'''
'''
std_image = tf.compat.v1.image.per_image_standardization(image)
print(np.array(std_image))
cv.imshow("result", np.array(std_image))
cv.waitKey(0)
'''
'''
图像归一化
'''
result = np.zeros(image.shape,dtype=np.float32)
cv.normalize(image,result,norm_type=cv.NORM_MINMAX,dtype=cv.CV_32F)
print(result)
cv.imshow("norm",np.uint8(result*255.0))
cv.waitKey(0)
cv.destroyAllWindows()
