#-*- coding: utf-8 -*-

import cv2
import sys
import gc
from face_train_use_keras import Model
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import faceTest
import time
import pymysql


string = ''




class search(QMainWindow):
    result = ""
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('查询')
        self.setFixedSize(800,800)
        self.box()
    
    def onclock(self,name):
        db = pymysql.connect(host='localhost', user='root', password='wwl133933', db='wwl', port=3306)
        cursor = db.cursor()
        result = None
        sql = "SELECT * FROM stafftimes WHERE name = '%s'" % (name)
        
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            db.commit() 
            print(result)
            
            
        except Exception as e:
            print("插入出错：case%s" % e)
        finally:
            cursor.close()
            db.close()
            self.text1.setText(str(result))
            return result
        
    

    
    def box(self):
        mainwidget = QWidget()

        flo=QFormLayout()
        self.langtext = QLineEdit()
        flo.addRow(self.langtext)
        self.bt1 = QPushButton("查询")
        self.text1 = QTextEdit()
        flo.addRow(self.bt1)
        flo.addRow(self.text1)

        self.bt1.setMaximumSize(100,100)
        self.bt1.clicked.connect(lambda: self.onclock(self.langtext.text()))

        mainwidget.setLayout(flo)
        self.setCentralWidget(mainwidget)

class signin(QMainWindow):


    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('注册')
        self.setFixedSize(540,500)
        self.box()
    

    def onclock(self,name,age,male,tele):
        db = pymysql.connect(host='localhost', user='root', password='wwl133933', db='wwl', port=3306)
        cursor = db.cursor()
        result = None
        print(name,age,tele,male)
        sql = "INSERT INTO staff VALUES ('%s','%s','%s','%s')"%(name,age,tele,male)
        
        try:
            cursor.execute(sql)
            db.commit() 
            
        except Exception as e:
            print("插入出错：case%s" % e)
        finally:
            cursor.close()
            db.close()

            return result


    def box(self):
        mainwidget = QWidget()

        flo=QFormLayout()
        self.langtext = QLineEdit()
        flo.addRow('姓名',self.langtext)
        self.langtext1 = QLineEdit()
        flo.addRow('性别',self.langtext1)
        self.langtext2 = QLineEdit()
        flo.addRow('年龄',self.langtext2)
        self.langtext3 = QLineEdit()
        flo.addRow('电话',self.langtext3)

        self.bt1 = QPushButton("注册")
        flo.addRow(self.bt1)
        self.bt1.setMaximumSize(100,100)

        self.langtext.setMaximumSize(300,50)
        self.langtext1.setMaximumSize(300,50)
        self.langtext2.setMaximumSize(300,50)
        self.langtext3.setMaximumSize(300,50)

        self.bt1.clicked.connect(lambda:self.onclock(self.langtext.text(),self.langtext2.text(),self.langtext1.text(),self.langtext3.text()))

        mainwidget.setLayout(flo)
        self.setCentralWidget(mainwidget)






class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('FaceRecognition')
        self.setFixedSize(800,800)
        self.add_menu()
    
    def onclock(self):
        faceTest.start()
    windowList = []
    def sign(self):
        win = signin()
        self.windowList.append(win)
        self.close
        win.show()
    def search(self):
        win = search()
        self.windowList.append(win)
        self.close
        win.show()


    def add_menu(self):
        self.bt = QPushButton('注册')
        self.bt1 = QPushButton('录入数据')
        self.bt2 = QPushButton('打卡')
        self.bt3 = QPushButton('查询')

        topLayout = QHBoxLayout()
        topLayout.addWidget(self.bt)
        topLayout.addWidget(self.bt1)
        topLayout.addWidget(self.bt2)
        topLayout.addWidget(self.bt3)
        self.text = QTextEdit()
        
        #self.bt1.clicked(print("1"))

        self.bt1.clicked.connect(self.onclock)
        self.bt2.clicked.connect(self.start)
        self.bt.clicked.connect(self.sign)
        self.bt3.clicked.connect(self.search)

        file = './res/wwl.txt'
        with open(file,'r') as f:
                string = f.read()
        self.text.setText(string)

        
        #QMainWindow的中心窗口部件
        mainwidget = QWidget()
        #创建布局
        layout = QHBoxLayout()
        #layout.addWidget(self.text)
        #self.text.setMaximumWidth(600)
        
        layout.addLayout(topLayout)
        mainwidget.setLayout(layout)
        self.setCentralWidget(mainwidget)


    def onclock(self,name,time):
        db = pymysql.connect(host='localhost', user='root', password='wwl133933', db='wwl', port=3306)
        cursor = db.cursor()
        result = None
        print(name,time)
        sql = "INSERT INTO stafftimes VALUES ('%s','%s')"%(name,time)
        
        try:
            cursor.execute(sql)
            db.commit() 
            
        except Exception as e:
            print("插入出错：case%s" % e)
        finally:
            cursor.close()
            db.close()
            
            return result
        

    def start(self):
        global string

        #加载模型
        model = Model()
        model.load_model(file_path = './model/me.face.model.h5')

        #框住人脸的矩形边框颜色
        color = (0, 255, 0)

        #捕获指定摄像头的实时视频流
        cap = cv2.VideoCapture(0)

        #人脸识别分类器本地存储路径
        cascade_path = "E:/Python/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"

        #循环检测识别人脸
        while True:
            _, frame = cap.read()   #读取一帧视频

            #图像灰化，降低计算复杂度
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #使用人脸识别分类器，读入分类器
            cascade = cv2.CascadeClassifier(cascade_path)

            #利用分类器识别出哪个区域为人脸
            faceRects = cascade.detectMultiScale(frame_gray, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
            id =''
            if len(faceRects) > 0:
                for faceRect in faceRects:
                    x, y, w, h = faceRect

                    #截取脸部图像提交给模型识别这是谁
                    image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                    faceID = model.face_predict(image)

                    #如果是“我”
                    if faceID == 0:
                        cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, thickness = 2)

                        #文字提示是谁
                        cv2.putText(frame,'KK',
                                    (x + 30, y + 30),                      #坐标
                                    cv2.FONT_HERSHEY_SIMPLEX,              #字体
                                    1,                                     #字号
                                    (255,0,255),                           #颜色
                                    2) #字的线宽
                        id = "KK"
                        
                                        
                    else:
                        cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, thickness = 2)

                        #文字提示是谁
                        cv2.putText(frame,'WWL',
                                    (x + 30, y + 30),                      #坐标
                                    cv2.FONT_HERSHEY_SIMPLEX,              #字体
                                    1,                                     #字号
                                    (255,0,255),                           #颜色
                                    2) #字的线宽
                        id = "wwl"

        
            cv2.imshow("faceRecognition", frame)

            #等待10毫秒看是否有按键输入
            k = cv2.waitKey(10)
            #如果输入q则退出循环
            if k & 0xFF == ord('='):
                localtime = time.asctime( time.localtime(time.time()) )
                print ("wwl的打卡时间为时间为 :", localtime)
                self.onclock(id,localtime)
                file = './res/wwl.txt'
                with open(file, 'a+') as f:
                    f.write(localtime+'\n')   #加\n换行显示
                break
                
        #释放摄像头并销毁所有窗口
        cap.release()
        cv2.destroyAllWindows()
'''
def jdbc():
    db = pymysql.connect(host='localhost', user='william', password='wwl133933', db='sys', port=3306)
    cursor = db.cursor()
    result = None
    sql = 'select `人员ID`,`姓名` from person_inform where `缩写`=\"'+abridge+'\"'
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
    except Exception as e:
        print("查询出错：case%s" % e)
    finally:
        cursor.close()
        db.close()
        return result
'''
def databases():
    db = pymysql.connect(host='localhost', user='root', password='wwl133933', db='wwl', port=3306)
    cursor = db.cursor()
    result = None
    sql = "SELECT * FROM staff"
       
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
    except Exception as e:
        print("查询出错：case%s" % e)
    finally:
        cursor.close()
        db.close()
        return result


if __name__ =='__main__':
    databases()
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
