import numpy as np
import math
from dip import *


class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        """Initialzes/Computes and returns a 5X5 Gaussian filter"""
        matrix = zeros((5, 5))
        sum = 0

        for i in range(5):
            for j in range(5):
                exponent = math.exp(-1 * ( ( (i-2)**2 + (j-2)**2 ) / (2) ) )
                value = (1/(2*math.pi)) * exponent
                sum += value
                matrix[i][j] = value

        return matrix, sum

    def get_laplacian_filter(self):
        """Initialzes and returns a 3X3 Laplacian filter"""
        laplacian = array([[0, 1, 0],
                           [1, -4, 1],
                           [0, 1, 0]])

        return laplacian

    def filter(self, filter_name):
        """Perform filtering on the image using the specified filter, and returns a filtered image
            takes as input:
            filter_name: a string, specifying the type of filter to use ["gaussian", laplacian"]
            return type: a 2d numpy array
                """
        final_image = np.zeros((self.image.shape[0], self.image.shape[1]), dtype=int)

        if filter_name == "gaussian":
            filter, sum = self.get_gaussian_filter()
            pad_size = filter.shape[0] // 2
            pad_img = zeros((self.image.shape[0] + 2 * pad_size, self.image.shape[1] + 2 * pad_size))
            pad_img[pad_size:-pad_size, pad_size:-pad_size] = self.image

            for i in range(pad_size, pad_img.shape[0]-pad_size):
                for j in range(pad_size, pad_img.shape[1]-pad_size):
                    value = 0
                    for x in range(filter.shape[0]):
                        for y in range(filter.shape[1]):
                            window = pad_img[i-pad_size+x, j-pad_size+y]
                            value += filter[x][y] * window
                    final_image[i-pad_size, j-pad_size] = value
            return final_image


        else:
            filter = self.get_laplacian_filter()
            pad_size = filter.shape[0] // 2
            pad_img = zeros((self.image.shape[0] + 2 * pad_size, self.image.shape[1] + 2 * pad_size))
            pad_img[pad_size:-pad_size, pad_size:-pad_size] = self.image

            for i in range(pad_size, pad_img.shape[0]-pad_size):
                for j in range(pad_size, pad_img.shape[1]-pad_size):
                    value = 0
                    for x in range(filter.shape[0]):
                        for y in range(filter.shape[1]):
                            window = pad_img[i-pad_size+x, j-pad_size+y]
                            value += filter[x][y] * window
                    final_image[i-pad_size, j-pad_size] = value

            return final_image

