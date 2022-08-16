import matplotlib.pyplot as plt 
import cv2
import numpy as np

def main():

    img_path='./jpg.jpg'
    rgb=plt.imread(img_path)

    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    plt.subplot(3,2,1)
    plt.imshow(gray,cmap='gray')

    hist_gray = cv2.calcHist([gray],[0],None,[256],[0,256])
    plt.subplot(3,2,2)
    plt.plot(hist_gray)


    equalization=cv2.equalizeHist(gray)
    plt.subplot(3,2,3)
    plt.imshow(equalization,cmap='gray')

    hist_equalization=cv2.calcHist([equalization],[0],None,[256],[0,256])
    plt.subplot(3,2,4)
    plt.plot(hist_equalization)

    plt.show()





if __name__ == '__main__':
    main()