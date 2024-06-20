import cv2 as cv
import numpy as np
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5 import QtGui



class SharpSobel():


    def SobelMask(self,ImaLoaded):

        #Apply Sobel filter in x direction(Horizontal edges)
        self.sobelx=cv.Sobel(ImaLoaded,cv.CV_64F,1,0, ksize=3)
        
        #Apply Sobel filter in y direction(Vertical edges)
        self.sobely=cv.Sobel(ImaLoaded,cv.CV_64F,0,1, ksize=3)

        #Combine the both filters
        self.SobelCombined=cv.magnitude(self.sobelx,self.sobely)

        #Normalize the magnitude in order to be in range of 0 to 255
        self.SobelCombined=cv.normalize(self.SobelCombined,None,0,255,cv.NORM_MINMAX)

        #make sure the values are in 8bits (0-255)
        self.SobelCombined=np.uint8(self.SobelCombined)


        #convert the image from BGR to a QImage
        #get image properties

        self.S_height , self.S_width=self.SobelCombined.shape
        self.S_bytesPerLine=self.S_width
        self.S_qImg=QtGui.QImage(self.SobelCombined.data,self.S_width,self.S_height,self.S_bytesPerLine,QImage.Format_Grayscale8)

        #create a pixmap from the QImage
        #create a scene object
        self.S_scene= QGraphicsScene()

        #create a pixmax object
        self.S_pixmap=QtGui.QPixmap.fromImage(self.S_qImg)

        #add the pixmax to the scene
        self.S_scene.addPixmap(self.S_pixmap)

        return self.S_scene
 
    #func for the sharp using fouerier trans. to apply a high pass filter
    def FourierSharp(self,ImagLoaded):
        #apply the discrete fourier transform
        dft=cv.dft(np.float32(ImagLoaded), flags=cv.DFT_COMPLEX_OUTPUT)
        dft_shifted=np.fft.fftshift(dft)

        #apply high pass filter
        rows,cols=ImagLoaded.shape #pack the image dimensions
        Center_row,Center_col=rows//2 , cols//2 #calculate the center
        #mask with "1" ones , which means that the signal will pass
        mask=np.ones((rows,cols,2), np.uint8)
        #Define a ratio
        Ratio=40
        #this means that in the center of the mask , the value is "0"
        #so in the center of the mask the low frequencies will be blocked
        mask[Center_row-Ratio:Center_row+Ratio,
             Center_col-Ratio:Center_col+Ratio]=0
        
        


        #Return the image to the spatial domain using inverse FT
        fshift = dft_shifted * mask
        f_ishift = np.fft.ifftshift(fshift)
        img_back = cv.idft(f_ishift)
        #After apply Inverse FT , there is a real part and an imaginary part
        #real part will be store in img_back[:, :, 0]
        #the imaginary part will be store here img_back[:, :, 1]
        #magnitude will calculate the magnitude of these parts
        img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])


        #Normalize the values In a range of 0-255
        img_back=cv.normalize(img_back,None,0,255,cv.NORM_MINMAX)
        img_back=np.uint8(img_back)


        #convert the image from BGR to a QImage
        #get image properties
        self.FT_height,self.FT_width=img_back.shape
        self.FT_bytesPerLine=self.FT_width
        self.FT_qImg=QtGui.QImage(img_back.data,self.FT_width,self.FT_height,self.FT_bytesPerLine,QImage.Format_Grayscale8)

        #create a pixmap from the QImage
        #create a scene object

        self.FT_scene=QGraphicsScene()

        #create apixmax to the scene
        self.FT_pixmap=QtGui.QPixmap.fromImage(self.FT_qImg)

        #add the pixmax to the scene
        self.FT_scene.addPixmap(self.FT_pixmap)

        return self.FT_scene
        
