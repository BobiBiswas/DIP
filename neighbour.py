import matplotlib.pyplot as plt 
import cv2
import numpy as np

def main():

    img_path='./jpg.jpg'
    rgb=plt.imread(img_path)
    plt.subplot(2,3,1)
    plt.imshow(rgb)
    

    gray =cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    plt.subplot(2,3,2)
    plt.imshow(gray,cmap='gray')

    kernel=np.ones((3,3),dtype=np.uint8)
    print('kernel: {}'.format(kernel))
    kernel2=np.array([[1,1,1],[2,3,4],[3,2,6]])
    print('kernel2: {}'.format(kernel2))

    img1=cv2.filter2D(gray,-1,kernel)
    plt.subplot(2,3,3)
    plt.imshow(img1,cmap='gray')
    
    img2=cv2.filter2D(gray,-1,kernel2)
    plt.subplot(2,3,4)
    plt.imshow(img2,cmap='gray')

    plt.show()
if __name__ == '__main__':
    main()