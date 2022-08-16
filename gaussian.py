# libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# open the image f
rgb = plt.imread('./jpg.jpg')

plt.figure(figsize=(20,20))
plt.subplot(4,4,1)
plt.imshow(rgb, cmap='gray')
plt.title('RGB')


#gray image
f = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
plt.subplot(4,4,2)
plt.imshow(f, cmap='gray')
plt.title('Gray')

# transform the image into frequency domain, f --> F
F = np.fft.fft2(f)
plt.subplot(4,4,3)
plt.imshow(np.log1p(np.abs(F)), cmap='gray')
plt.title('FFT')

Fshift = np.fft.fftshift(F)
plt.subplot(4,4,4)
plt.imshow(np.log1p(np.abs(Fshift)), cmap='gray')
plt.title('Centered')


# Create Gaussin Filter: Low Pass Filter
M,N = f.shape
H = np.zeros((M,N), dtype=np.float32)
D0 = 10
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        H[u,v] = np.exp(-D**2/(2*D0*D0))


plt.subplot(4,4,4)
plt.imshow(H, cmap='gray')
plt.title('Gaussian')


# Image Filters
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

plt.subplot(4,4,5)
plt.imshow(np.log1p(np.abs(Gshift)), cmap='gray')
plt.title('FFT & Gaussian Low')

plt.subplot(4,4,6)
plt.imshow(g, cmap='gray')
plt.title('Apply Filter')


# Gaussian: High pass filter
HPF = 1 - H
plt.subplot(4,4,7)
plt.imshow(HPF, cmap='gray')
plt.title('High pass')


# Image Filters
Gshift = Fshift * HPF
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

plt.subplot(4,4,8)
plt.imshow(g, cmap='gray')
plt.title('Apply Filter')


plt.rcParams.update({'font.size': 12})	
plt.tight_layout()
plt.show()

