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



