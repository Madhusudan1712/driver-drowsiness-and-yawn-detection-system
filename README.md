# driver-drowsiness-and-yawn-detection-system
<- Aim of the Project ->
 
- To detect drowsiness driver and alert the driver through alarm system.
- Scope of the Project:
- In this project, we will focus on these following procedures: Basic concept of drowsiness detection system, Familiarize with the signs of drowsiness.
- Determine the drowsiness from these parameters: Eye blink, Area of the pupils detected at eyes, Yawning.

<- IMPLEMENTATION! ->

- EYE DETECTION
- In the system we have used facial landmark prediction for eye detection. Facial landmarks are used to localize and represent salient regions of the face, such as: Eyes, Eyebrows, Nose, Mouth, Jawline.
- Facial landmarks have been successfully applied to face alignment, head pose estimation, face swapping, blink detection and much more. In the context of facial landmarks, our goal is detecting important facial structures on the face using shape prediction methods. Detecting facial landmarks is therefore a two-step process: Localize the face in the image, Detect the key facial structures on the face ROI, Localize the face in the: image: The face image is localized by Haar feature-based cascade.
- There are a variety of facial landmark detectors, but all methods essentially try to localize and label the following facial regions: Mouth, Right eyebrow, Left eyebrow, Right eye , Left eye, Nose.
- This method starts by using:
A training set of labeled facial landmarks on an image. These images are manually Labeled, specifying specific (x. y)-coordinates of regions surrounding each facial structure. Priors of more specifically, the probabilily on distance between pairs of input pixels. The pre-trained facial landmark detector inside the lib library is used 10 estimate the location of 68 (x. y)-coordinates that map 10 facial structures on the face. The indexes of the 68 coordinates can be visualized in the image below:

![image](https://github.com/Madhusudan1712/driver-drowsiness-and-yawn-detection-system/assets/146712964/abd3aae2-a2bd-4673-b030-e87ba42a6a83)

- We detect and access both the eye region by the following facial landmark index shown below: The right eye using (37, 42) , The left eye with (43. 48).
- EYE STATE DETERMINATION: Finally, the decision for the eye state is made based on EAR calculated in the previous step. If the distance is zero or is close to zero, the eye state is classified as "closed" otherwise the eye state is identified as "open".
- DROWSINESS DETECTION: The last step of the algorithm is to determine the person's condition based on a pre-set condition for drowsiness. The average blink duration of a person is 100-400 milliseconds (i.e., 0.1-0.4 of a second). Hence if a person is drowsy his eye closure must be beyond this interval. We set a time frame of 5 seconds. If the eyes remain closed for five or more seconds, drowsiness is detected and alert pop regarding this is triggered.
- YAWNING DETECTION METHOD: Yawning detection method which can be used in drivers’ fatigue monitoring is proposed. To adapt to the variance in different mouth shapes and sizes, it based on mouth inner contour corner detection and curve fitting. First, the Harris corner detection algorithm was used to detect inner mouth feature points. Second, we established the open mouths’ mathematical model by curve fitting those points, calculated the degree of mouth openness using the mouth model, and generated the real-time M-curve. Third, the duration of big openness in successive images is divided into levels for further judgment. The validation results show that the method can obtain more precise mouth parameters and distinguish yawn from complex mouth activities. So the method achieves a higher level of accuracy.
- ALGORITHMS: 1.Haar-Cascade algorithm , 2.Eye Aspect Ratio (EAR) Algorithm
- HAAR-CASCADE ALGORITHM:
- Step 1: Load the required XML classifiers
- Step 2: Load our input video in grayscale mode
- Step 3: Find the faces in the image. If faces are found, it returns the positions of detected faces as Rect (x,y,w,h)
- Step 4: Get the locations and create a ROI (Region of interest) for the face and apply eye detection on this ROI
- Haar Cascade is a feature-based object detection algorithm to detect objects from images. A cascade function is trained on lots of positive and negative images for detection. The algorithm does not require extensive computation and can run in real-time. We can train our own cascade function for custom objects like animals, cars, bikes, etc. Haar Cascade can’t be used for face recognition since it only identifies the matching shape and size. Haar cascade uses the cascade function and cascading window. It tries to calculate features for every window and classify positive and negative. If the window could be a part of an object, then positive, else, negative.
- EYE ASPECT RATIO(EAR): It is an elegant solution that involves a very simple calculation based on the ratio of distances between facial landmarks of the eyes. Each eye is represented by 6 (x, y)- coordinates, starting at the left-corner of the eye and then working clockwise around the remainder of the region.
![image](https://github.com/Madhusudan1712/driver-drowsiness-and-yawn-detection-system/assets/146712964/f4506eab-09bb-44d2-acac-b1fcbcd5c6f0)
The following formula is used for calculation of EAR:
![image](https://github.com/Madhusudan1712/driver-drowsiness-and-yawn-detection-system/assets/146712964/ac1ecf7d-b3f5-438d-81cd-9ffb80f867de)
![image](https://github.com/Madhusudan1712/driver-drowsiness-and-yawn-detection-system/assets/146712964/ebefdcca-d232-4406-9f74-aac570fa3026)















