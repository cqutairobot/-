import cv2

img = cv2.imread("count.jpg",1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,binary  = cv2.threshold(gray,150,225,cv2.THRESH_BINARY_INV)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

erosion = cv2.erode(binary,kernel,iterations=4)
dilation = cv2.dilate(erosion,kernel,iterations=3)
gaussian = cv2.GaussianBlur(dilation,(3,3),0)

contours,hirearchy = cv2.findContours(gaussian,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contoursOK = []
for i in contours:
    if cv2.contourArea(i)>30:
        contoursOK.append(i)

draw = cv2.drawContours(img,contoursOK,-1,(0,255,0),1)

for i,j in zip(contoursOK,range(len(contoursOK))):
    M = cv2.moments(i)  
    cX = int(M["m10"]/M["m00"])
    cY = int(M["m01"]/M["m00"])
    cv2.putText(draw,str(j),(cX,cY),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255),2)
cv2.imshow("draw",draw)
cv2.imshow("gaussian",gaussian)

cv2.waitKey()
cv2.destroyAllWindows()