import matplotlib.pyplot as plt 
import numpy as np  
import cv2 

def main():
    img_path='./lenna.jpeg'
    rgb=plt.imread(img_path)

    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    plt.subplot(4,4,1)
    plt.imshow(gray,cmap='gray')

    r,c=gray.shape

    left,right,narrow=gray.copy(),gray.copy(),gray.copy()

    left=left -79
    plt.subplot(4,4,2)
    plt.imshow(left,cmap='gray')

    right=right+50
    plt.subplot(4,4,3)
    plt.imshow(right,cmap='gray')

    for i in range(r):
        for j in range(c):
            if narrow[i][j]<=100:
                narrow[i][j]=100
            elif narrow[i][j]>=175:
                narrow[i][j]=175
    plt.subplot(4,4,4)
    plt.imshow(narrow,cmap='gray')
    
    gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
    plt.subplot(4,4,5)
    plt.plot(gray_hist)

    left_hist=cv2.calcHist([left],[0],None,[256],[0,256])
    plt.subplot(4,4,6)
    plt.plot(left_hist)

    right_hist=cv2.calcHist([right],[0],None,[256],[0,256])
    plt.subplot(4,4,7)
    plt.plot(right_hist)

    narrow_hist=cv2.calcHist([narrow],[0],None,[256],[0,256])
    plt.subplot(4,4,8)
    plt.plot(narrow_hist)

    img_set=[gray,left,right,narrow,gray_hist,left_hist,right_hist,narrow_hist]
    
    # for i in range(8):
    #     plt.subplot(4,4,i+1)
    #     ch=len(img_set[i].shape)
    #     if(ch<=4):
    #         plt.imshow(img_set[i],cmap='gray')
    #     else:
    #         plt.plot(img_set[i])
    plt.show()


if __name__ =='__main__':
    main()