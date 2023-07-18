import cv2
import numpy as np

lena = cv2.imread("..\img\lenacolor.png")
cv2.imshow("lena",lena)

roi = lena[220:400,250:350]
key = np.random.randint(0,256,size=lena.shape,dtype=np.uint8)
lenaXorKey = cv2.bitwise_xor(lena,key)
secretFace = lenaXorKey[220:400,250:350]
cv2.imshow("secretFace",secretFace)

lena[220:400,250:350] = secretFace
enFace = lena
cv2.imshow("enFace",enFace)

extractOriginal = cv2.bitwise_xor(enFace,key)
face = extractOriginal[220:400,250:350]
cv2.imshow("face",face)

enFace[220:400,250:350] = face
deFace = enFace
cv2.imshow("deFace",deFace)

cv2.waitKey()
cv2.destroyAllWindows()