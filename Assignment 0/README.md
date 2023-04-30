# Digital Image Processing 
## Assignment - 0 ##

Due Date: Tue 02/07/23 11:59 PM


**1.  Image Merging:**

(10 pts.) Write code to merge the color image and black-and-white image of the apple.

![merged_image](https://user-images.githubusercontent.com/73811127/215221035-22163dc9-2521-4696-81c6-cc1c46966a1a.png)

The inputs to your function are: (i) blackwhite image: blackwhite_image.png (size: 183 Rows X 275 Cols), (ii) color image: color_image.png (size: 183 Rows X 275 Cols), (iii) image column (c) at which the images should be merged.

  - image_op/operations.py: Edit the function merge
    - Define a new image as follows: the first c columns (default value = 149) should be used from the left image (color\_image.png). The remaining columns should be used from the right image (blackwhite\_image.png).
    - Note that the blackwhite_image.png is not a greyscale image (with one channel) but a color image and has three channels with shape (183, 275, 3).
    
**2.  Color Slicing:**

(20 pts.) Write code to create a color sliced image from a color image. The overall objective is to extract pixels that have color that are similar to a predefined target color.
Each pixel in the final color sliced image is created by either populating the pixel from the color image or the black-and-white image.
The final color sliced image should copy pixels from the color image as long as the pixel's color distance to the target color is within a predefined threshold. If the distance is greater that the thershold, pixels from the black-and-white image are copied.    
Below is the expected output image. 

![color_extracted_image](https://user-images.githubusercontent.com/73811127/214874749-ee5f5354-bca9-4736-a6c0-981a942359cd.png)

*Inputs*: The inputs to your function are: (i) a color image: color\_image.png, (ii) blackwhite image: blackwhite\_image.png, (iii) the targeted color ((0, 0, 255) by default) and (iv) a threshold (t = 180 by default). 

  - image_op/operations.py: Edit the function color\_slicing.    
    + Create a result/output image of the same shape as the input color image
    + Calculate the Euclidean distance between every pixel of the color image and the target color.
    + If the distance is smaller than threshold, copy the color pixel, else copy the black-and-white pixel to the output image.
      
**Note:**
We are **restricted from importing cv2, numpy, stats and other third party libraries,** 
with the only exception of math, importing math library is allowed (import math).

While you can import it for testing purposes, the final submission should not contain the following statements.
- import cv2
- import numpy
- import numpy as np
- import stats
- etc...

The essential functions for the assignment are available in dip module one can import using the following statement
```
import dip
from dip import *
```
The following functions are available

```commandline
from cv2 import namedWindow, imshow, waitKey, imwrite, imread

from numpy import zeros, ones, array, shape, arange
from numpy import random
from numpy import min, max
from numpy import int, uint8, float, complex
from numpy import inf
from numpy.fft import fft2
```

*Assigments that contain any files that import these libraries will not be graded.* 
*Assigments that modify the dip.py file will not be graded.*
   
  - Please do not change the code structure
  - Usage:
   
        - python dip_hw0.py -ic <image-name> -ib <image2-name> -c <column> -t <threshold> -tc <target-color-blue> -tc <target-color-green> -tc <target-color-red>
        - Example: python dip_hw0.py -ic color_image.png -ib blackwhite_image.png -c 149 -t 180 -tc 0 -tc 0 -tc 255
   
  where `c = column`, `t = threshold`, `tc = blue_value green_value red_value`. You can change the values of the arguments as you may want.

  - Please make sure the code runs when you run the above command from prompt/terminal
  - All the output images and files are saved to "output/" folder

Two images are provided for testing: blackwhite_image.png and color_image.png
  
PS. Please do not change dip.py, dip_hw0.py, requirements.txt, and Jenkinsfile. 


1. Operation      - 30 Pts.

    Total         - 30 Pts.


-----------------------

<sub><sup>
License: Property of Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston. This software is property of the QIL, and should not be distributed, reproduced, or shared online, without the permission of the author This software is intended to be used by students of the digital image processing course offered at the University of Houston. The contents are not to be reproduced and shared with anyone without the permission of the author. The contents are not to be posted on any online public hosting websites without the permission of the author. The software is cloned and is available to the students for the duration of the course. At the end of the semester, the Github organization is reset and hence all the existing repositories are reset/deleted, to accommodate the next batch of students.
</sub></sup>


