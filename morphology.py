import matplotlib.pyplot as plt 
import numpy as np
import cv2

def main():
    img_path='./lenna.jpeg'
    rgb=plt.imread(img_path)
    plt.subplot(4,4,1)
    plt.imshow(rgb)

    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    plt.subplot(4,4,2)
    plt.imshow(gray,cmap='gray')

    kernel=np.ones((3,3))

    erosion=cv2.erode(gray,kernel=kernel,iterations=1)
    plt.subplot(4,4,3)
    plt.imshow(erosion,cmap='gray')

    dilation=cv2.dilate(gray,kernel=kernel,iterations=1)
    plt.subplot(4,4,4)
    plt.imshow(dilation,cmap='gray')

    opening=cv2.morphologyEx(gray,cv2.MORPH_OPEN,kernel=kernel)
    plt.subplot(4,4,5)
    plt.imshow(opening,cmap='gray')

    closing=cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel=kernel)
    plt.subplot(4,4,6)
    plt.imshow(closing,cmap='gray')

    # img_set=[rgb,gray,erosion,dilation,opening,closing]
    # n=len(img_set)
    # for i in range(n):
    #     plt.subplot(2,3,i+1)
    #     ch=len(img_set[i].shape)
    #     if(ch==3):
    #         plt.imshow(img_set[i],cmap='gray')
    #     else:
    #         plt.plot(img_set[i])
    plt.show()

if __name__ == '__main__':
    main()