import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path='./jpg.jpg'
    rgb=plt.imread(img_path)
    plt.subplot(3,3,1)
    plt.imshow(rgb)

    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    plt.subplot(3,3,2)
    plt.imshow(gray,cmap='gray')
    
    F=np.fft.fft2(gray)
    plt.subplot(3,3,3)
    plt.imshow(np.log1p(np.abs(F)),cmap='gray')

    Fshift=np.fft.fftshift(F)
    plt.subplot(3,3,4)
    plt.imshow(np.log1p(np.abs(Fshift)),cmap='gray')

    m,n=gray.shape
    H=np.zeros((m,n),dtype=np.uint8)
    D0=50
    for u in range(m):
        for v in range(n):
            D=np.sqrt((u-m/2)**2+(v-n/2)**2)
            if D<=D0:
                H[u,v]=1
            else:
                H[u,v]=0
    plt.subplot(3,3,5)
    plt.imshow(H,cmap='gray')

    gshift=Fshift*H
    plt.subplot(3,3,6)
    plt.imshow(np.log1p(np.abs(gshift)),cmap='gray')

    g=np.abs(np.fft.ifft2(gshift))
    plt.subplot(3,3,7)
    plt.imshow(g,cmap='gray')


    plt.show()
if __name__=='__main__':
    main()