Drowsiness detection system is regarded as an effective tool to reduce the number of road accidents. This project proposes a non-intrusive approach for detecting drowsiness in drivers, using Computer Vision. Developing various technologies for monitoring and preventing drowsiness while driving is a major trend and challenge in the domain of accident avoidance systems. Haar face detection algorithm is used to capture frames of image as input and then the detected face as output. Haar feature based Adaboost algorithm is used to extract the facial region from the image.Facial landmarks are used to extract the draw contours around the eyes and mouth of the driver. EAR and MAR values are calculated and if their values exceed a certain threshold, the user/driver is alerted to be in a state of drowsiness.Head tilt is estimated to determine the drivers attention on the road.



The algorithm is coded on OpenCV platform in Linux environment. The parameters considered to detect drowsiness are face and eye detection, blinking, eye closure and head tilt . The algorithm is Haar trained to detect the face. Once the face is detected, the facial landmarks position around the eyes and mouth are determined. For Facial Landmarks download the 'shape_predictor_68_face_landmarks.dat' easily available on github . Contains trained Facial Landmarks Detector


The larger the dataset better would be the cascade classifier.Training a Haar cascade classifier requires high computation power and patience.Though LBP is quicker HaarCascades Classifier achieves better accuracy.For Training we referred :https://docs.opencv.org/3.4.1/dc/d88/tutorial_traincascade.html .

For  Head tilt refer :https://www.learnopencv.com/head-pose-estimation-using-opencv-and-dlib/
