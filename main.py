from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
from PyQt5.QtWidgets import QFileDialog
from Smooth_Filter import *
from Sharp import *
from GaussianFil import *
from GaussianFourier import *



class Ui_MainWindow(object):
    def __init__(self):
        self.LoadImage= ''
        #self.ima=None
        

    def setupUi(self, MainWindow):
        #MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920,1080)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        #Backgroud Color
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("""
        QWidget#centralwidget {
            background-color: #FF6B6B; 
        }
        """)
        

        # QTextEdit para mostrar mensajes de error
        self.errorLog = QtWidgets.QTextEdit(self.centralwidget)
        self.errorLog.setGeometry(QtCore.QRect(20, 10, 490, 180))  
        self.errorLog.setObjectName("errorLog")
        font = QtGui.QFont("Microsoft YaHei", 16)  
        self.errorLog.setFont(font)

        #Load Image Button
        self.pushButton_LoadImage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LoadImage.setGeometry(QtCore.QRect(62, 210, 436, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.pushButton_LoadImage.setFont(font)
        self.pushButton_LoadImage.setObjectName("pushButton_3")

        #Smooth Filter Button
        self.pushButton_SmootFilter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SmootFilter.setGeometry(QtCore.QRect(62, 370, 436, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.pushButton_SmootFilter.setFont(font)
        self.pushButton_SmootFilter.setObjectName("pushButton_4")

        #Sharp Button
        self.pushButton_Sharp_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sharp_5.setGeometry(QtCore.QRect(62, 525, 436, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.pushButton_Sharp_5.setFont(font)
        self.pushButton_Sharp_5.setObjectName("pushButton_5")

        #Gaussian Button
        self.pushButton_Gaussian_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Gaussian_6.setGeometry(QtCore.QRect(62, 680, 436, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.pushButton_Gaussian_6.setFont(font)
        self.pushButton_Gaussian_6.setObjectName("pushButton_6")

        #Lower Pass Button  
        self.pushButton_GaussianFD_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GaussianFD_7.setGeometry(QtCore.QRect(62, 840, 436, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.pushButton_GaussianFD_7.setFont(font)
        self.pushButton_GaussianFD_7.setObjectName("pushButton_7")

        #Original Image
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(516, 15, 683, 433))
        self.graphicsView.setObjectName("graphicsView")

        #Image up right quadrant
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(1218, 15, 683, 433))
        self.graphicsView_2.setObjectName("graphicsView_2")

        #Image down left quadrant
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(516, 521, 683, 433))
        self.graphicsView_3.setObjectName("graphicsView_3")

        #Image down right quadrant
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(1218, 521, 683, 433))
        self.graphicsView_4.setObjectName("graphicsView_4")


        #Labels

        #Original Image Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(760, 464, 312, 46))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #Image up right quadrant Label
        self.label_Gview_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Gview_2.setGeometry(QtCore.QRect(1540, 462, 167, 46))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.label_Gview_2.setFont(font)
        self.label_Gview_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Gview_2.setObjectName("label_2")

        #Image down left quadrant Label
        self.label_Gview_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_Gview_3.setGeometry(QtCore.QRect(820, 950, 210, 46))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.label_Gview_3.setFont(font)
        self.label_Gview_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Gview_3.setObjectName("label_3")

        #Image down right quadrant Label
        self.label_Gview_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_Gview_4.setGeometry(QtCore.QRect(1540, 950, 167, 46))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.label_Gview_4.setFont(font)
        self.label_Gview_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Gview_4.setObjectName("label_4")

        #set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_LoadImage.setText(_translate("MainWindow", "Load Image"))
        self.pushButton_SmootFilter.setText(_translate("MainWindow", "Smooth Filter"))
        self.pushButton_Sharp_5.setText(_translate("MainWindow", "Sharp"))
        self.pushButton_Gaussian_6.setText(_translate("MainWindow", "Gaussian"))
        self.pushButton_GaussianFD_7.setText(_translate("MainWindow", "Lower Pass"))
        self.label.setText(_translate("MainWindow", "Original Image"))
        self.label_Gview_2.setText(_translate("MainWindow", "Image"))
        self.label_Gview_3.setText(_translate("MainWindow", "Image"))
        self.label_Gview_4.setText(_translate("MainWindow", "Image"))



        ###create SmoothFilter object
        self.SmFl= SmoothFilter() 

        ###create Sobel sharp object
        self.Sharp=SharpSobel()

        ###create the object for the gaussian script
        self.GaussFil=GaussianFilter()

        ###create the object for the gaussian filter in the frequency domain
        self.GaussFD=GaussianFourierTrans()



        #activate the buttons
        #Smooth filters buttons
        self.pushButton_LoadImage.clicked.connect(self.LoadImage_func)
        self.pushButton_SmootFilter.clicked.connect(self.MedianFilterAct)
        self.pushButton_SmootFilter.clicked.connect(self.AverageFilterAct)
        self.pushButton_SmootFilter.clicked.connect(self.FourierTransAct)

        #Sharp filters buttons
        self.pushButton_Sharp_5.clicked.connect(self.SobelMaskAct)
        self.pushButton_Sharp_5.clicked.connect(self.FourierSharpAct)
        
        self.pushButton_Gaussian_6.clicked.connect(self.GaussianFilterAct)
        self.pushButton_GaussianFD_7.clicked.connect(self.GaussianFrequencyDom_Act)
        self.pushButton_GaussianFD_7.clicked.connect(self.GaussianFrequencyDom_Act_FD)



    #Load image function
    def LoadImage_func(self):
        try:
            
            self.LoadImage = QFileDialog.getOpenFileName()[0]

            if self.LoadImage:
            
                #load the image
                self.ima=cv.imread(self.LoadImage, cv.IMREAD_GRAYSCALE)

                #convert the image from BGR to a QImage
                #get image properties
                self.height, self.width= self.ima.shape
                self.bytesPerLine= self.width
                self.qImg= QtGui.QImage(self.ima.data, self.width, self.height, self.bytesPerLine, QImage.Format_Grayscale8)

                #create a pixmap from the QImage
                #create a scene object
                self.scene= QGraphicsScene()

                #create a pixmap object
                self.pixmap= QtGui.QPixmap.fromImage(self.qImg)

                #add the pixmap to the scene
                self.scene.addPixmap(self.pixmap)

                #set the scene to the graphicsView
                self.graphicsView.setScene(self.scene)
                self.graphicsView.show()

                #Make sure that Other GraphicsView windows are empty and restore their labels
                #Reset GraphicsView and label 2
                self.graphicsView_2.setScene(None)
                self.graphicsView_2.show()
                self.label_Gview_2.setText("Image")
                self.label_Gview_2.setGeometry(QtCore.QRect(1540, 462, 167, 46))
                
                #Reset GraphicsView and label 3
                self.graphicsView_3.setScene(None)
                self.graphicsView_3.show()
                self.label_Gview_3.setText("Image")
                self.label_Gview_3.setGeometry(QtCore.QRect(820, 950, 210, 46))

                #Reset GraphicsView and label 4
                self.graphicsView_4.setScene(None)
                self.graphicsView_4.show()
                self.label_Gview_4.setText("Image")
                self.label_Gview_4.setGeometry(QtCore.QRect(1540, 950, 167, 46))



            else:
                errorMessage=f"You did not or could not load any image"
                self.errorLog.setText(errorMessage)
                
        except Exception as e:
            errorMessage=f"An error occurred when you upload the image.\n"\
                        f"{e}\n"\
                        "Check that the image is not corrupted,\n"\
                         "the folder does not have Chinese chars or special chars\n"\
                             
            self.errorLog.setText(errorMessage)


    #This is the fuction with activates the Median Filter
    def MedianFilterAct(self):
        #Manage Errors
        try:
            #Check if image is loaded
            if self.ima is not None:
                
                self.scene_Median=self.SmFl.Median_filter(self.ima)

                #set the scene to the graphicsView
                self.graphicsView_3.setScene(self.scene_Median)
                self.graphicsView_3.show()

                #update label Text and Geometry
                update_label="1(a) Median filter"
                self.label_Gview_3.setText(update_label)
                self.label_Gview_3.setGeometry(QtCore.QRect(750, 950, 210, 46))

            else:
                errorMessage=f"An error occurred when you upload the image!!\n"\
                                "Please check before push any buttons"
                self.errorLog.setText(errorMessage)

        except Exception as e:
            errorMessage=f"You have not uploaded any image yet!!\n"\
                                "Please upload an image before push filter buttons."
            self.errorLog.setText(errorMessage)


    #This is the function that activates the Average filter
    def AverageFilterAct(self):
        #First manage errors to avoid the program get closed
        try:
            #check if the image is loaded
            if self.ima is not None:

                self.scene_Average=self.SmFl.Average_filter(self.ima)

                #set the scene to the graphicsView
                self.graphicsView_2.setScene(self.scene_Average)
                self.graphicsView_2.show()

                #update label Text and Geometry
                update_label="1(a) Average filter"
                self.label_Gview_2.setText(update_label)
                self.label_Gview_2.setGeometry(QtCore.QRect(1470, 462, 210, 46))

            else:
                errorMessage=f"An error occurred when you upload the image!!\n"\
                                "Please check before push any buttons"
                self.errorLog.setText(errorMessage)


        except Exception as e:
            errorMessage=f"You have not uploaded any image yet!!\n"\
                                "Please upload an image before push filter buttons."
            self.errorLog.setText(errorMessage)
            
        
        
    #This is the function that activates The Fourier Trasn, with the low-pass filter
    def FourierTransAct(self):
        #First manage errors to avoid the program get closed
        try:
            #check if the image is loaded
            if self.ima is not None:

                self.scene_Fouriertrans=self.SmFl.Fourier_trans(self.ima)

                #set the scene to the graphicsView
                self.graphicsView_4.setScene(self.scene_Fouriertrans)
                self.graphicsView_4.show()

                #update label Text and Geometry
                update_label="1(b) Fourier transform"
                self.label_Gview_4.setText(update_label)
                self.label_Gview_4.setGeometry(QtCore.QRect(1460, 950, 250, 46))

            else:
                errorMessage=f"An error occurred when you upload the image!!\n"\
                                "Please check before push any buttons"
                self.errorLog.setText(errorMessage)


        except Exception as e:
            errorMessage=f"You have not uploaded any image yet!!\n"\
                                "Please upload an image before push filter buttons."
            self.errorLog.setText(errorMessage)
            

    #this function is to activate the sobel mask
    def SobelMaskAct(self):
        #First manage errors to avoid the program get closed
        try:
            #check if the image is loaded
            if self.ima is not None:

                self.scene_SobelMaskS=self.Sharp.SobelMask(self.ima)

                #set the scene to the graphicsView
                self.graphicsView_3.setScene(self.scene_SobelMaskS)
                self.graphicsView_3.show()

                #update label Text and Geometry
                update_label="2(a) Sobel mask"
                self.label_Gview_3.setText(update_label)
                self.label_Gview_3.setGeometry(QtCore.QRect(750, 950, 210, 46))

                self.graphicsView_2.setScene(None)
                self.graphicsView_2.show()
                self.label_Gview_2.setText("No use")
                self.label_Gview_2.setGeometry(QtCore.QRect(1540, 462, 210, 46))

            else:
                errorMessage=f"An error occurred when you upload the image!!\n"\
                                "Please check before push any buttons"
                self.errorLog.setText(errorMessage)


        except Exception as e:
            errorMessage=f"You have not uploaded any image yet!!\n"\
                                "Please upload an image before push filter buttons."
            self.errorLog.setText(errorMessage)


    #Activate the sharp,the high pass filter in the frequency domain
    def FourierSharpAct(self):
         #First manage errors to avoid the program get closed
        try:
            #check if the image is loaded
            if self.ima is not None:
                
                #call the func FourierSharp from sharp script
                self.Scene_FourierSharp=self.Sharp.FourierSharp(self.ima)

                #set the scene to the graphicsView
                self.graphicsView_4.setScene(self.Scene_FourierSharp)
                self.graphicsView_4.show()
                #update label Text and Geometry
                update_label="2(b) Fourier transform"
                self.label_Gview_4.setText(update_label)
                self.label_Gview_4.setGeometry(QtCore.QRect(1460, 950, 250, 46))

            else:
                errorMessage=f"An error occurred when you upload the image!!\n"\
                                "Please check before push any buttons"
                self.errorLog.setText(errorMessage)


        except Exception as e:
            errorMessage=f"You have not uploaded any image yet!!\n"\
                                "Please upload an image before push filter buttons."
            self.errorLog.setText(errorMessage)


    #Func to activate the gaussian filter
    def GaussianFilterAct(self):
         #First manage errors to avoid the program get closed
        try:
            #check if the image is loaded
            if self.ima is not None:
                
                #call the func Gaussian_filter from GaussianFil script
                self.Scene_GaussianFil=self.GaussFil.Gaussian_filter(self.ima)

                #set the scene to the graphicsView
                self.graphicsView_2.setScene(self.Scene_GaussianFil)
                self.graphicsView_2.show()
                #update label Text and Geometry
                update_label="Gaussian Filter(Spatial Domain\n\
                    Low-pass)"
                self.label_Gview_2.setText(update_label)
                self.label_Gview_2.setGeometry(QtCore.QRect(1470, 462,310, 46))

                #Reset GraphicsView and label 3
                self.graphicsView_3.setScene(None)
                self.graphicsView_3.show()
                self.label_Gview_3.setText("No use")
                self.label_Gview_3.setGeometry(QtCore.QRect(820, 950, 210, 46))

                #Reset GraphicsView and label 4
                self.graphicsView_4.setScene(None)
                self.graphicsView_4.show()
                self.label_Gview_4.setText("No use")
                self.label_Gview_4.setGeometry(QtCore.QRect(1540, 950, 210, 46))

            else:
                errorMessage=f"An error occurred when you upload the image!!\n"\
                                "Please check before push any buttons"
                self.errorLog.setText(errorMessage)


        except Exception as e:
            errorMessage=f"You have not uploaded any image yet!!\n"\
                                "Please upload an image before push filter buttons."
            self.errorLog.setText(errorMessage)

    

    
   #Func to activate the gaussian low pass filter in the spatial domain 
    def GaussianFrequencyDom_Act(self):
        #First manage errors to avoid the program get closed
        try:
            #check if the image is loaded
            if self.ima is not None:
                
                #call the func GaussianFrequencyDomain 
                #from the GaussianFourier script
                self.Scene_GaussianFD_Fil=self.GaussFD.GaussianFrequencyDomain(self.ima)

                #set the scene to the graphicsView
                self.graphicsView_2.setScene(self.Scene_GaussianFD_Fil)
                self.graphicsView_2.show()
                #update label Text and Geometry
                update_label="Gaussian Filter(Frequency Domain\n\
                    Low-pass)"
                self.label_Gview_2.setText(update_label)
                self.label_Gview_2.setGeometry(QtCore.QRect(1470, 462,350, 46))

                

                #Reset GraphicsView and label 4
                self.graphicsView_4.setScene(None)
                self.graphicsView_4.show()
                self.label_Gview_4.setText("No use")
                self.label_Gview_4.setGeometry(QtCore.QRect(1540, 950, 210, 46))

            else:
                errorMessage=f"An error occurred when you upload the image!!\n"\
                                "Please check before push any buttons"
                self.errorLog.setText(errorMessage)


        except Exception as e:
            errorMessage=f"You have not uploaded any image yet!!\n"\
                                "Please upload an image before push filter buttons."
            self.errorLog.setText(errorMessage)
        
     #Func to activate the gaussian low pass filter in the Frequency
    def GaussianFrequencyDom_Act_FD(self):
        #First manage errors to avoid the program get closed
        try:
            #check if the image is loaded
            if self.ima is not None:
                
                #call the func GaussianFrequencyDomain 
                #from the GaussianFourier script
                self.Scene_GaussianFD_Fil_2=self.GaussFD.GaussianFrequencyDomain_FD(self.ima)

                #set the scene to the graphicsView
                self.graphicsView_3.setScene(self.Scene_GaussianFD_Fil_2)
                self.graphicsView_3.show()
                #update label Text and Geometry
                update_label="Gaussian Fil(In the Frequency Domain)"
                self.label_Gview_3.setText(update_label)
                self.label_Gview_3.setGeometry(QtCore.QRect(680, 950, 400, 46))


            else:
                errorMessage=f"An error occurred when you upload the image!!\n"\
                                "Please check before push any buttons"
                self.errorLog.setText(errorMessage)


        except Exception as e:
            errorMessage=f"You have not uploaded any image yet!!\n"\
                                "Please upload an image before push filter buttons."
            self.errorLog.setText(errorMessage)
        
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
