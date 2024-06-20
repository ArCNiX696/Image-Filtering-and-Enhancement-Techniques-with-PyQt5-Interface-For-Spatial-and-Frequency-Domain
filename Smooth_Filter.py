#from main import ui
import cv2 as cv
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5 import QtWidgets,QtGui
import numpy as np


class SmoothFilter():
    
    #Media Filter function
    def Median_filter(self,LoadedImg):
        
        #Apply the median filter
        self.ima_filtered=cv.medianBlur(LoadedImg,5)
        
        #convert the image from BGR to a QImage
        #get image properties

        self.M_height , self.M_width=self.ima_filtered.shape
        self.M_bytesPerLine=self.M_width
        self.M_qImg=QtGui.QImage(self.ima_filtered.data,self.M_width,self.M_height,self.M_bytesPerLine,QImage.Format_Grayscale8)

        #create a pixmap from the QImage
        #create a scene object
        self.M_scene= QGraphicsScene()

        #create a pixmax object
        self.M_pixmap=QtGui.QPixmap.fromImage(self.M_qImg)

        #add the pixmax to the scene
        self.M_scene.addPixmap(self.M_pixmap)

        return self.M_scene



    def Average_filter(self,LoadedIma):
        #Apply the average Filter
        self.avr_filter_ima=cv.blur(LoadedIma,(5,5))

        #convert the image from BGR to a QImage
        #get image properties

        self.A_height,self.A_width=self.avr_filter_ima.shape
        self.A_bytesPerLine=self.A_width
        self.A_qImg=QtGui.QImage(self.avr_filter_ima.data,self.A_width,self.A_height,self.A_bytesPerLine,QImage.Format_Grayscale8)

        #create a pixmap from the QImage
        #create a scene object

        self.A_scene=QGraphicsScene()

        #create apixmax to the scene
        self.A_pixmap=QtGui.QPixmap.fromImage(self.A_qImg)

        #add the pixmax to the scene
        self.A_scene.addPixmap(self.A_pixmap)

        return self.A_scene


    def Fourier_trans(self,LoadImg):
        #Calculate the Discrete fourier Transform
        dtf=cv.dft(np.float32(LoadImg),flags=cv.DFT_COMPLEX_OUTPUT)
        dft_shift=np.fft.fftshift(dtf)

       #Create a circular mask for the low pass filter
       #Get num of rows an cols of the imag
        rows,columns=LoadImg.shape

        #calculate the  center of the spectrum
        Center_row,Center_column=rows//2,columns//2

        #Create a mask of zeros,2 layers, one for the real part
        #One layer for the imaginari part
        mask=np.zeros((rows,columns,2),np.uint8)

        #set the ratio for the low pass circle
        #low ratio results in a more blur image 
        #big ratio let more hihg frequencies pass the filter
        #in consecuence, the image is not too blur but less preccesed
        Ratio=60

        #the mask depends of the ratio, for example if the ratio is biger
        #the area of the mas will be bigger, and the values of that area
        #will be equal 1, so it will not modift  the original signal
        #in consecuence more low frequences will pass the filter
        #frequencies outside the ratio will be block since the value is 0
        mask[Center_row-Ratio:Center_row+Ratio,
             Center_column-Ratio:Center_column+Ratio]=1
        

        #Apply the mask on the signal of FT
        #dft_shift is the variable that contains that signal
        fshift=dft_shift*mask

        #Return the image into the spatial domain using Inverse FT
        f_ishift=np.fft.ifftshift(fshift)
        img_sd=cv.idft(f_ishift)
        img_sd=cv.magnitude(img_sd[:,:,0],img_sd[:,:,1])

        #Normalize the values In a range of 0-255
        cv.normalize(img_sd,img_sd,0,255,cv.NORM_MINMAX)
        img_sd=np.uint8(img_sd)

        #convert the image from BGR to a QImage
        #get image properties
        self.FT_height,self.FT_width=img_sd.shape
        self.FT_bytesPerLine=self.FT_width
        self.FT_qImg=QtGui.QImage(img_sd.data,self.FT_width,self.FT_height,self.FT_bytesPerLine,QImage.Format_Grayscale8)

        #create a pixmap from the QImage
        #create a scene object

        self.FT_scene=QGraphicsScene()

        #create apixmax to the scene
        self.FT_pixmap=QtGui.QPixmap.fromImage(self.FT_qImg)

        #add the pixmax to the scene
        self.FT_scene.addPixmap(self.FT_pixmap)

        return self.FT_scene




        




        


    
         
            

            





        

        
