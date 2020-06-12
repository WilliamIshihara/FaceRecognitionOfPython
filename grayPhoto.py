import numpy as np
import cv2
import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt
import os


#灰度化照片并存储


def showimg(img, isgray=False):
  plt.axis("off")
  if isgray == True:
    plt.imshow(img, cmap='gray')
  else: 
    plt.imshow(img)
  plt.show()
'''
def getimg(filename):
  return Image.open("G:/Code/python/faceRecognition/photos/wwl/"+filename)


#img = cv2.imread('G:/Code/python/faceRecognition/photos/wwl/0.jpg')




#print(img.shape)
#print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Y = 0.299R + 0.587G + 0.114B
print("cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)结果如下：")
print('大小:{}'.format(gray_img.shape))
print("类型：%s" % type(gray_img))
print(gray_img)

if __name__ =='__main__':
  num = 0
  for readname in os.listdir("./photos/wwl"):
    im = getimg(readname)
    im_gray = im.convert('L')
    img_name = '%s/%d.jpg' % ("./photos/wwl2", num)
    cv2.imwrite(img_name,im_gray)
    num += 1
    #showimg(im_gray, True)
'''

def grayImag():
  for readname in os.listdir("./photos/wwl"):
    img = cv2.imread("G:/Code/python/faceRecognition/photos/wwl/"+readname)
    GrayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #showimg(GrayImg,True)
    cv2.imwrite("G:/Code/python/faceRecognition/photos/wwl2/"+readname,GrayImg)


