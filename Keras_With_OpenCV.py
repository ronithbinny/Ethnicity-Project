import cv2
import os
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

classifier = Sequential()

classifier.add(Conv2D(32,(3,3), input_shape = (64,64,1)))

classifier.add(MaxPooling2D(pool_size = (2,2)))

classifier.add(Flatten())

classifier.add(Dense(units = 128, activation = "relu"))

classifier.add(Dense(units = 256, activation = "relu"))

classifier.add(Dense(units = 512, activation = "relu"))

classifier.add(Dense(units = 21, activation = "softmax"))

classifier.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])


from keras.preprocessing.image import ImageDataGenerator

train_data = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip= True)

test_data = ImageDataGenerator(rescale = 1./255)

training_set = train_data.flow_from_directory("People", target_size = (64,64), batch_size = 32, class_mode = "categorical", color_mode = "grayscale")

test_set = test_data.flow_from_directory("Faces", target_size = (64,64), batch_size = 32, class_mode = "categorical", color_mode = "grayscale")

classifier.fit_generator(training_set, samples_per_epoch = 13447, nb_epoch = 25, validation_data = test_set, nb_val_samples = 4819)

# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
# From Web Cam :
cap = cv2.VideoCapture(0)

while True :
    
    _, frames = cap.read()
        
    cv2.imshow("Web-Cam", frames)
        
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
    path_test = r"C:\Users\Ronith\Desktop\Data Science 2020\Projects\Ethnicity Project\Keras\test01.jpg"
        
    frames = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        
        # Locating Face : 
    faces = face_cascade.detectMultiScale(frames, 1.3, 3)
    
    if len(faces) == 1 :
        for (x,y,w,h) in faces :
            frames = frames [y:w+y,x:h+x]
        
        cv2.imwrite(path_test,frames)
            
        x = cv2.imread(path_test)
        
        x = cv2.resize(x,(64,64))
            
        grey = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
            
        X = grey.reshape(1,64,64,1)
            
        pred = classifier.predict_classes(X)
        
        xxx = os.listdir(r'C:\Users\Ronith\Desktop\Data Science 2020\Projects\Ethnicity Project\Keras\Faces')
            
        print(xxx[pred[0]])
            
    else :
        print("Face Not Detected")
        
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
