import cv2

A=cv2.imread("limg\ena1.bmp",0)
B=cv2.imread("img\watermark.bmp",0)

C=B.copy()
w=C[:,:]>0
C[w]=1

D=A*C
E=255-B
F=D+E
cv2.imshow("A",A)
cv2.imshow("B",B)
cv2.imshow("C",C*255)
cv2.imshow("D",D)
cv2.imshow("E",E)
cv2.imshow("F",F)
cv2.waitKey()
cv2.destroyAllWindows()