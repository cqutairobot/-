import cv2
import numpy as np

lena = cv2.imread("..\img\lenacolor.png")
cv2.imshow("lena",lena)

mask = np.zeros(lena.shape,dtype=np.uint8)
mask [220:400,250:350] = 1
key = np.random.randint(0,256,size=lena.shape,dtype=np.uint8)
lenaXorKey = cv2.bitwise_xor(lena,key)
encryptFace = cv2.bitwise_and(lenaXorKey,mask*255)
noFacel = cv2.bitwise_and(lena,(1-mask)*255)
maskFace = encryptFace + noFacel
cv2.imshow("maskFace",maskFace)


extractOriginal = cv2.bitwise_xor(maskFace,key)
extractFace = cv2.bitwise_and(extractOriginal,mask*255)
noFace2 = cv2.bitwise_and(maskFace,(1-mask)*255)

extractLena = extractFace +noFace2

cv2.imshow("extractLena",extractLena)
cv2.waitKey()
cv2.destroyAllWindows()
