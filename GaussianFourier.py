import numpy as np
from PyQt5.QtGui import QImage
from PyQt5 import QtGui
from PyQt5.QtWidgets import QGraphicsScene
import cv2 as cv



class GaussianFourierTrans():
    def __init__(self):
        #standard deviation
        self.sigma=10.0
    

    def GaussianFrequencyDomain(self,Loaded_img):

        #apply the discrete fourier transform
        dft=cv.dft(np.float32(Loaded_img), flags=cv.DFT_COMPLEX_OUTPUT)
        dft_shifted=np.fft.fftshift(dft)


        ###Gaussian Low pass filter
        rows,cols=Loaded_img.shape

        x_val=np.linspace(-cols//2,cols//2,cols)
        y_val=np.linspace(-rows//2,rows//2,rows)

        x,y=np.meshgrid(x_val,y_val)

        kernel_formu=np.exp(-0.5*(np.square(x)+np.square(y))/np.square(self.sigma))

        kernel=kernel_formu/np.sum(kernel_formu)

        kernel = kernel[:, :, np.newaxis]


        #apply the filter on the image
        fshift = dft_shifted * kernel
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
        GFD_height,GFD_width=img_back.shape
        bytesPerLine=GFD_width
        GFD_qImg=QtGui.QImage(img_back.data,GFD_width,GFD_height,bytesPerLine,QImage.Format_Grayscale8)

        #create a pixmap from the QImage
        #create a scene object

        GFD_scene=QGraphicsScene()

        #create apixmax to the scene
        GFD_pixmap=QtGui.QPixmap.fromImage(GFD_qImg)

        #add the pixmax to the scene
        GFD_scene.addPixmap(GFD_pixmap)

        return GFD_scene
        


    def GaussianFrequencyDomain_FD(self, Loaded_img):
        # Apply Fourier Transform
        dft = cv.dft(np.float32(Loaded_img), flags=cv.DFT_COMPLEX_OUTPUT)
        dft_shifted = np.fft.fftshift(dft)

        # Gussian low pass filter
        rows, cols = Loaded_img.shape
        x_val = np.linspace(-cols//2, cols//2, cols)
        y_val = np.linspace(-rows//2, rows//2, rows)
        x, y = np.meshgrid(x_val, y_val)
        
        # Kernel
        kernel_formu = np.exp(-0.5 * (np.square(x) + np.square(y)) / np.square(self.sigma))
        kernel = kernel_formu / np.sum(kernel_formu)
        kernel = kernel[:, :, np.newaxis]

        #Apply the kernel on the Image
        fshift = dft_shifted * kernel

        magnitude_spectrum = 20 * np.log(cv.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

        # Normalize the values in order to be in a range of 0-255
        magnitude_spectrum = cv.normalize(magnitude_spectrum, None, 0, 255, cv.NORM_MINMAX)
        magnitude_spectrum = np.uint8(magnitude_spectrum)

        # convert the image in gray scale format
        bytesPerLine = cols
        GFD_qImg = QtGui.QImage(magnitude_spectrum.data, cols, rows, bytesPerLine, QtGui.QImage.Format_Grayscale8)

        # Create a Qpixmap scene to display the processed image 
        GFD_scene = QGraphicsScene()
        GFD_pixmap = QtGui.QPixmap.fromImage(GFD_qImg)
        GFD_scene.addPixmap(GFD_pixmap)

        return GFD_scene

        



    
    
