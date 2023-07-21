import cv2
#读取原始载体图像
lena=cv2.imread("lenacolor.png")
#读取水印图像
watermark=cv2.imread("watermark.bmp",1)
#按位或运算
e=cv2.bitwise_or(lena,watermark)
#============显示============
cv2.imshow("lena",lena)
cv2.imshow("watermark",watermark)   
cv2.imshow("bitwise_or",e)
#============释放============
cv2.waitKey()
cv2.destroyAllWindows()