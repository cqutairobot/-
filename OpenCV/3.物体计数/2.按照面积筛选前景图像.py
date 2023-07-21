import cv2
o = cv2.imread('img\opencv.png')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
 
contoursOK=[]  
for i in contours:
     if cv2.contourArea(i)>1000: 
        contoursOK.append(i)
cv2.drawContours(o,contoursOK,-1,(0,0,255),8) 
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()