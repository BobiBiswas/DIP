import matplotlib.pyplot as plt 
import cv2
import numpy as np 

def main():
    img_path='./jpg.jpg'
    rgb=plt.imread(img_path)
    
    gray=cv2.cvtColor(rgb,cv2.COLOR_BGR2GRAY)

    r,c =gray.shape


    bit1=np.zeros((r,c),dtype=np.uint8)
    bit2=np.zeros((r,c),dtype=np.uint8)
    bit3=np.zeros((r,c),dtype=np.uint8)
    bit4=np.zeros((r,c),dtype=np.uint8)
    bit5=np.zeros((r,c),dtype=np.uint8)
    bit6=np.zeros((r,c),dtype=np.uint8)
    bit7=np.zeros((r,c),dtype=np.uint8)
    bit8=np.zeros((r,c),dtype=np.uint8)

    k=1
    for i in range(r):
        for j in range(c):
            bit1[i][j]=gray[i][j] & k

            bit2[i][j]=gray[i][j] & (k<<1)
            bit3[i][j]=gray[i][j] & (k<<2)
            bit4[i][j]=gray[i][j] & (k<<3)
            bit5[i][j]=gray[i][j] & (k<<4)
            bit6[i][j]=gray[i][j] & (k<<5)
            bit7[i][j]=gray[i][j] & (k<<6)
            bit8[i][j]=gray[i][j] & (k<<7)


    img_set=[rgb,gray,bit1,bit3,bit3,bit4,bit5,bit6,bit7,bit8]
    
    plt.figure(figsize=(15,15))
    for i in range(10):
        plt.subplot(4,3,i+1)
        
        ch=len(img_set[i].shape)
        if(ch==3):
            plt.imshow(img_set[i],cmap='gray')

        else:
            plt.imshow(img_set[i],cmap='gray')




    plt.show()




if __name__ == '__main__':
    main()
