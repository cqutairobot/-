import cv2
import numpy as np

lena = cv2.imread("..\img\lena1.bmp",0)
cv2.imshow("lena",lena)

r,c = lena.shape
x = np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i] = 2**i
ri = np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    ri[:,:,i] = cv2.bitwise_and(lena,x[:,:,i])
    ri[ri[:,:,i]>0] =255
    cv2.imshow(str(i),ri[:,:,i])
cv2.waitKey()
cv2.destroyAllWindows()    

