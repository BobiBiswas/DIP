import matplotlib.pyplot as plt 
import cv2
import numpy as np

def main():

    img_path =('./jpg.jpg')
    rgb=plt.imread(img_path)
    

    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
   

    n,m=gray.shape
    mask=np.zeros((n,m),dtype=np.uint8)
    
    for i in range(300,500):
        for j in range(200,400):
            mask[i][j]=255

    
    mask_image=cv2.bitwise_and(gray,gray,mask=mask)
    
    img_set=[rgb,gray,mask,mask_image]
    title_set=['rgb','gray','mask','mask_image']
    plt.figure(figsize=(15,15))
    for i in range(4):
        plt.subplot(2,3,i+1)
        plt.title(title_set[i])
        ch=len(img_set[i].shape)
        if(ch==3):
            plt.imshow(img_set[i],cmap='gray')

        else:
            plt.imshow(img_set[i],cmap='gray')




    plt.show()
if __name__ == '__main__':
    main()