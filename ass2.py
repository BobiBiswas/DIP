import matplotlib.pyplot as plt 
import cv2 
import numpy as np

def main():
    img_path ='./jpg.jpg'
    rgb=plt.imread(img_path)
    plt.subplot(2,3,1)
    plt.imshow(rgb,cmap='gray')

    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    plt.subplot(2,3,2)
    plt.imshow(gray,cmap='gray')

    r,c=gray.shape
    img1=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    T1=70
    T2=150

    for i in range(r):
        for j in range(c):
            if gray[i][j]>=T1 and gray[i][j]<=T2:
                img1[i][j]=100
            else:
                img1[i][j]=10

    plt.subplot(2,3,3)
    plt.imshow(img1,cmap='gray')

    img2=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    for i in range(r):
        for j in range(c):
            if gray[i][j]>=T1 and gray[i][j]<=T2:
                img2[i][j]=100
            

    plt.subplot(2,3,4)
    plt.imshow(img2,cmap='gray')

    img3=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    k=2
    for i in range(r):
        for j in range(c):
            img3[i][j]=k*np.log(1+gray[i][j])

    plt.subplot(2,3,5)
    plt.imshow(img3,cmap='gray')

    img4=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    p=3
    ep=.0000001
    for i in range(r):
        for j in range(c):
            img4[i][j]=k*(gray[i][j]+ep)**p

    plt.subplot(2,3,6)
    plt.imshow(img4,cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()