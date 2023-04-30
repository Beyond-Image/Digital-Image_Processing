# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv

import numpy as np
from dip import *


class Filtering:

    def __init__(self, image):
        """initializes the variables for frequency filtering on an input image
        takes as input:
        image: the input image
        """
        self.image = image
        self.mask = self.get_mask

    def get_mask(self, shape):
        """Computes a user-defined mask
        takes as input:
        shape: the shape of the mask to be generated
        rtype: a 2d numpy array with size of shape
        """
        mask = ones(shape, uint8)

        for x in range(275, 294):
            for y in range(202, 225):
                mask[x][y] = 0
        for x in range(240, 249):
            for y in range(230, 242):
                mask[x][y] = 0
        for x in range(265, 274):
            for y in range(272, 282):
                mask[x][y] = 0
        for x in range(222, 241):
            for y in range(289, 310):
                mask[x][y] = 0

        return mask

    def post_process_image(self, image):
        """Post processing to display DFTs and IDFTs
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        You can perform post processing as needed. For example,
        1. You can perfrom log compression
        2. You can perfrom a full contrast stretch (fsimage)
        3. You can take negative (255 - fsimage)
        4. etc.
        """

        image_min = np.amin(image)
        image_max = np.amax(image)
        normalized = (image - image_min) / (image_max - image_min)

        #log compression
        compressed = np.log(1 + normalized * 255) / np.log(256)

        int_img = compressed.astype(np.uint8)

        return int_img

    def filter(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering
        ----------------------------------------------------------
        You are allowed to use inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do post processing on the magnitude and depending on the algorithm (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8
        """

        fft = fftshift(fft2(self.image))
        
        magnitude = np.abs(fft)
        compressed = np.log(1 + magnitude) * 10 
        compressed = compressed.astype('uint8')
        
        mask = self.get_mask(compressed.shape)
        filtered = compressed * mask

        magrestore = np.exp(filtered / 10) - 1
        DFTrestore = magrestore * np.exp(1j * np.angle(fft))
        restoredshift = ifftshift(DFTrestore)
        restored = ifft2(restoredshift).real


        return [restored, compressed, filtered]
