# Panorama_cv
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




