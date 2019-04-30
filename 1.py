import os
import cv2
from matplotlib import pyplot as plt
from operator import add 
import csv
import time
i=1
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

c={}
cv2.namedWindow("detection")
 # load initial image
temp=os.listdir(".")
with open('haar.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow('name','actual' ,'predicted'])
#print()
    while True:
#img = cv2.imread(temp[i],0)
        if(temp[i].endswith("jpg")):
            img = cv2.imread('Abdullah_Gul_0010.jpg')
    
            gray = cv2.cvtColor(img, 1)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
    
            cv2.imshow("lala", img)

            k = chr(cv2.waitKey())
            if k == 'y':                       # toggle current image
                
                if temp[i] not in c: 
                    c[temp[i]]="y"
                
                    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([temp[i],'y' ,'y'])
                i+=1
            elif k == 'n':                       # toggle current image
                
                if temp[i] not in c:
                    c[temp[i]]="n"
                    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([temp[i],'y', 'n'])
                i+=1
            elif k == 'q':
                break
    

print(c)
cv2.destroyAllWindows()