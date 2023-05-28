# Computer-Vision-works

This repository is created for archieving works from computer vision works.   
It composes to [panorama-making](https://github.com/dripdropdr/computer-vision-works#panorama_cv), [cartoonize](https://github.com/dripdropdr/computer-vision-works#cartoonize_cv), [camera-calibration and pose-estimation](https://github.com/dripdropdr/computer-vision-works#camera-calibration-on-a_cv).



## Panorama_cv
This is a program for making panorama image using opencv.   
Stitcher combine multiple images to single seamless panorama image.  
The steps are following:
   1. Extract feature from all images
   2. Select m candidate matching images that have the most feature matches to one image
   3. Find geometrically consistent feature matches to solve for the homography between pairs of images.
   4. Find connected components of image matches.
   5. Perform transformation.   
   
---

- Run
   ```sh
   python panorama_cv.py IMAGEPATH1 IMAGEPATH2 ... 
   ```
   
- Results

*Input*

<img src=https://user-images.githubusercontent.com/81093298/225485312-bddeb7af-a3e5-4fdd-9f6a-3bf676146d71.jpg height=200px/> <img src=https://user-images.githubusercontent.com/81093298/225485307-e8e9b9a2-b592-4ce6-8a65-fc75c001a54c.jpg height=200px/> <img src=https://user-images.githubusercontent.com/81093298/225485314-31784ccc-fba6-4eae-9585-0128b0bd131f.jpg height=200px/>

*Output*

<img src=https://user-images.githubusercontent.com/81093298/225485303-dbd2cbbd-4d60-477b-967e-f956aeb91d60.jpg height=350px/>



## cartoonize_cv
Program to cartoonize real photo.   
For catoonzie, we use 1) constrast stretching and 2) k-means clustering. 
1) increase the contrast of image.
<img src=https://user-images.githubusercontent.com/81093298/228492242-00d43362-9ad6-43e2-a95a-4f4672d63220.png height=300px/>
2) clustering the color of image into K groups. This code defined the K to 5.
<img src=https://user-images.githubusercontent.com/81093298/228492936-7664fe1e-7e28-41a4-9327-d60c20f18fe7.png height=300px/>

---

- Run
   ```sh
   python photo_to_cartoon.py INPUTIMAGE
   ```
   
- Results

*Input*

<img src=https://user-images.githubusercontent.com/81093298/228485310-eae6ed9a-e24b-42ac-b12a-d9030f440a2b.jpeg width=500px/>

*Output*

<img src=https://user-images.githubusercontent.com/81093298/228488239-8eddf832-7384-4cef-a2c3-7844aa0ececf.jpeg width=500px/>

*ChatGPT*

<img src=https://user-images.githubusercontent.com/81093298/228615985-b0c0dda4-4780-4131-8c31-a84647f7e1a7.jpeg width=500px/>
it combines edge and blurred image.



## Camera-calibration-on-A_cv

The program that calibrate chessboard video and put A on chessboard.   

_Input_   
<img height="500" alt="input1" src="https://user-images.githubusercontent.com/81093298/235342173-e15ffc30-aa40-4955-afe9-64ce11f4d562.png"> <img height="500" alt="input2" src="https://user-images.githubusercontent.com/81093298/235342177-57d4817b-2a1e-4008-83d0-65e15017f356.png">

_Output_   
<img height="500" alt="result1" src="https://user-images.githubusercontent.com/81093298/235342178-e678119a-356d-4d77-b15e-61606d05b4ee.png"><img height="500" alt="result2" src="https://user-images.githubusercontent.com/81093298/235342180-0fb55537-9004-4df9-a8e7-6801d1cd2b06.png">
---
- Run
   ```sh
   python camera_calibration_on_A.py VIDEOPATH
   ```
  
If you change the shooting direction of video, the position of A change, too.

After performing the simple AR, omits the calibration results. 

### Camera Calibration Results (example)
* RMS error = 0.3674050821064493
* Camera matrix (K) = 
[[1.64016431e+03 0.00000000e+00 5.70771387e+02]
 [0.00000000e+00 1.64380630e+03 9.91567459e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]   
 (focal length = 1.64e+03, principal point x = 5.70771387e+02, principal point y = 9.91567459e+02)
* Distortion coefficient (k1, k2, p1, p2, k3, ...) = [ 0.2012792  -1.13786191  0.00828182  0.00496422  2.28385296]
