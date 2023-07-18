import cv2
import numpy as np
lena = cv2.imread("..\img\lena1.bmp",0)
r,c = lena.shape
t1 = np.ones((r,c),dtype=np.uint8)*254
lsb0 = cv2.bitwise_and(lena,t1)
w = cv2.imread("..\img\watermark.bmp",0)
wt = w.copy()
wt[w>0]=1

wo = cv2.bitwise_or(lsb0,wt)
t2 = np.ones((r,c),dtype=np.uint8)
ewb = cv2.bitwise_and(wo,t2)
ew = ewb
ew[ewb>0] = 255

cv2.imshow("lena",lena)
cv2.imshow("watermask",w)
cv2.imshow("wo",wo)
cv2.imshow("ew",ew)
cv2.waitKey()
cv2.destroyAllWindows()