import cv2
import numpy as np

lena = cv2.imread("..\img\lenacolor.png")

key = np.random.randint(0,256,size=lena.shape,dtype=np.uint8)
encryption = cv2.bitwise_xor(lena,key)
decryption = cv2.bitwise_xor(encryption,key)

cv2.imshow("lena",lena)
cv2.imshow("key",key)
cv2.imshow("encryption",encryption)
cv2.imshow("decryption",decryption)

cv2.waitKey()
cv2.destroyAllWindows()