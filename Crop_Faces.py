import cv2
import os

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

diri = r"C:\Users\Ronith\Desktop\Data Science 2020\Projects\Ethnicity Project\Dataset\Croped Faces - OPENCV\downloads"

for lis in os.listdir(diri) :
    i = 0
    dirix = r"C:\Users\Ronith\Desktop\Data Science 2020\Projects\Ethnicity Project\Dataset\Croped Faces - OPENCV\downloads\{}".format(lis)
    print(lis)
    for images in os.listdir(dirix) :
        
        try :
    
            img = cv2.imread("downloads\{}\{}".format(lis,images))
            print(images)
            grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade.detectMultiScale(grey, 1.5, 4)
            
            for (x,y,w,h) in faces :
                #cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                #print(x,y,w,h)
                crop_img = img[y:y+h, x:x+w]
                cv2.imwrite("Faces\{}\{}.jpg".format(lis,i),crop_img)
                i = i + 1
                print(i)
        except :
            pass
