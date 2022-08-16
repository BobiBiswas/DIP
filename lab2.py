import matplotlib.pyplot as plt 
import numpy as np 
import  cv2

def main():

    img_path='./jpg.jpg'
    rgb=plt.imread(img_path)
    print(rgb.shape)
    # plt.subplot(2,2,1)
    # plt.imshow(rgb)
    # plt.show()

    gray =cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    plt.subplot(2,2,1)
    plt.imshow(gray,cmap='gray')
    # hist_gray=cv2.calcHist(gray,[0],None,[256],[0,256])
    # plt.subplot(2,2,2)
    # plt.plot(hist_gray)


    '''negative by 1st way point processing'''
    process_img1=255-gray
    plt.subplot(2,2,3)
    plt.imshow(process_img1,cmap='gray')

    '''negative by 2nd way point processing'''
    r,c =gray.shape
    process_img2=np.zeros((r,c),dtype=np.uint8)
    for x in range(r):
        for y in range(c):
            process_img2[x,y]=255-gray[x,y]
    plt.subplot(2,2,4)
    plt.imshow(process_img2,cmap='gray')

    plt.show()


if __name__ == '__main__':
    main()