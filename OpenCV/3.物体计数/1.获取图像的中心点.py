import cv2
o = cv2.imread('img\cat3.jpg',1) 
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
x=cv2.drawContours(o,contours,0,(0,0,255),3)
m00=cv2.moments(contours[0])['m00']
m10=cv2.moments(contours[0])['m10']
m01=cv2.moments(contours[0])['m01']
cx=int(m10/m00)
cy=int(m01/m00)
cv2.putText(o, "cat", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255),3)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()