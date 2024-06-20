import numpy as np
from scipy.ndimage import convolve
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5 import QtGui
import cv2 as cv


class GaussianFilter():
    def __init__(self):
        self.sigma=90.0 #Standard deviation
        self.Mask_size=5 #adjust this adjust the mask at  5x5
        
        

    def Gaussian_filter(self,imag_loaded):
        #create the gaussian filter
        #this create 2 matrix (x,y) with linspace values
        #in range -1 to 1
        x,y=np.meshgrid(np.linspace(-1,1,self.Mask_size),
                        np.linspace(-1,1,self.Mask_size))
        
        #Apply the formula of the Gaussian filter
        gaussian=np.exp(-(x**2+y**2)/(2*self.sigma**2))
        
        #this is to normalize so the sum of all the values
        # in the filter will be equal 1 
        filter=(gaussian/gaussian.sum())
        #print(filter)

        ####in the spatial domain you should use the convolution 
        #of the filter across the image
        convolved_imag=convolve(imag_loaded,filter)

        ##This print is just to verify if the values are Int values from 0-255
        #print(f"These are the values of convolved_imag:\n {convolved_imag}")
        ######

        
        self.G_height , self.G_width=convolved_imag.shape
        self.G_bytesPerLine=self.G_width
        self.G_qImg=QtGui.QImage(convolved_imag.data,self.G_width,self.G_height,self.G_bytesPerLine,QImage.Format_Grayscale8)

        #create a pixmap from the QImage
        #create a scene object
        self.G_scene= QGraphicsScene()

        #create a pixmax object
        self.G_pixmap=QtGui.QPixmap.fromImage(self.G_qImg)

        #add the pixmax to the scene
        self.G_scene.addPixmap(self.G_pixmap)

        return self.G_scene
    

   

    