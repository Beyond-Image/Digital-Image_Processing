import math
from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """
        # new code
        # add your code here

        lenrow = len(image_left)
        lencol = len(image_left[0])
        merge_image = zeros((lenrow, lencol, 3), uint8)

        merge_image[0:lenrow, 0:column] = image_left[0:lenrow, 0:column]
        merge_image[0:lenrow, column:lencol] = image_right[0:lenrow, column:lencol]

        # Please do not change the structure
        return merge_image  # Currently the original image is returned, please replace this with the merged image

    def color_slicing(self, color_image, blackwhite_image, target_color, threshold):
        """
        Perform color slicing to create an image where only the targeted color is preserved and the rest
        is black and white

        color_image: the input color image
        blackwhite_image: the input black and white image
        target_color: the target color to be extracted
        threshold: the threshold to determine the pixel to determine the prximity to the target color

        return: output_image
        """

        #possible color values 0-255
        
        # add your code here

        lenrow = len(color_image)
        lencol = len(color_image[0])
        merge_image = zeros((lenrow, lencol, 3), uint8)

        testing = color_image[0, 0:3]

        for x in range(lenrow):
            for y in range(lencol):
                holder = color_image[x, y]
                distance = math.sqrt((holder[0]-target_color[0])**2 + (holder[1]-target_color[1])**2 + (holder[2]-target_color[2])**2)
                if distance <= threshold:
                    merge_image[x, y] = holder
                else:
                    merge_image[x, y] = blackwhite_image[x, y]
                        

        # final = gray_image * mask_in


        # Please do not change the structure
        return merge_image # Currently the input image is returned, please replace this with the color extracted image

   