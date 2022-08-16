import matplotlib.pyplot as plt 
import cv2
import numpy as np 

def main():

    img_path='./jpg.jpg'
    rgb=plt.imread(img_path)
    print(rgb.shape)
    # hist_rgb=cv2.calcHist(rgb,[0],None,[256],[0,256])
    # plt.subplot(2,2,1)
    # plt.plot(hist_rgb)
    # plt.subplot(2,2,2)
    # plt.imshow(rgb)
    # plt.show()
    # '''
    red=rgb[:,:,0]
    hist_rgb=cv2.calcHist(red,[0],None,[256],[0,256])
    plt.subplot(2,2,1)
    plt.plot(hist_rgb)
    plt.subplot(2,2,2)
    plt.imshow(rgb)
    plt.show()
    # green=rgb[:,:,1]
    # blue=rgb[:,:,2]

    # gray=.299*red +.587*green+.114*blue
    # print(gray.shape)
    # plt.subplot(2,2,2)
    # plt.imshow(gray,cmap='gray')
    # '''

    # gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    # #plt.subplot(2,2,3)
    # #plt.imshow(gray,cmap='gray')

    # binary=cv2.threshold(gray,50,255,cv2.THRESH_BINARY)[1]
    # #plt.subplot(2,2,4)
    # #plt.imshow(binary,cmap='gray')

    # img_set=[rgb,gray,binary]
    # title_set=['rgb','gray','binary']
    # plt.figure(figsize=(20,20))
    # for i in range(3):
    #     plt.subplot(2,2,i+1)
    #     plt.title(title_set[i])
    #     ch=len(img_set[i].shape)
    #     if(ch==3):
    #         plt.imshow(img_set[i],cmap='gray')
    #     else:
    #        plt.imshow(img_set[i],cmap='gray') 
    
    # plt.show()







if __name__ =='__main__':
    main()