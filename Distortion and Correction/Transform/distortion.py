from configparser import Interpolation
from operator import iconcat
from .interpolation import interpolation
from dip import *
import math

class Distort:
    def __init__(self):
        pass

    def distortion(self, image, k):
        """Applies distortion to the image
                image: input image
                k: distortion Parameter
                return the distorted image"""
        lenrow = len(image)
        lencol = len(image[0])
        distored_image = zeros((lenrow, lencol, 3), uint8)

        center_x = lenrow/2
        center_y = lencol/2

        for x in range(lenrow):
            for y in range(lencol):
                ic = x - center_x
                jc = y - center_y

                rad = math.sqrt(ic**2 + jc**2)

                icd = (1/(1+k*rad))*ic
                jcd = (1/(1+k*rad))*jc

                i_d = (icd + center_x)
                j_d = (jcd + center_y)

                #distored_image[i_d, j_d] = image[x, y]
                distored_image[round(i_d), round(j_d)] = image[x, y]

        return distored_image

    def correction_naive(self, distorted_image, k):
        """Applies correction to a distorted image by applying the inverse of the distortion function
        image: the input image
        k: distortion parameter
        return the corrected image"""

        lenrow = len(distorted_image)
        lencol = len(distorted_image[0])

        center_x = lenrow/2
        center_y = lencol/2
        corrected_image = zeros((lenrow, lencol, 3), uint8)

        for x in range(lenrow):
            for y in range(lencol):
                ic = x - center_x
                jc = y - center_y

                rad = math.sqrt(ic**2 + jc**2)

                icd = ((1 + (k*rad)) * ic)
                jcd = ((1 + (k*rad)) * jc)

                i = round(icd + center_x)
                j = round(jcd + center_y)
         
                if(i < lenrow-1 and j < lencol-1 and i > 0 and j > 0):
                        corrected_image[i, j] = distorted_image[x, y]

        return corrected_image

    def correction(self, distorted_image, k, interpolation_type):
        """Applies correction to a distorted image and performs interpolation
                image: the input image
                k: distortion parameter
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the corrected image"""
        lenrow = len(distorted_image)
        lencol = len(distorted_image[0])

        center_x = lenrow/2
        center_y = lencol/2

        corrected_image = zeros((lenrow, lencol, 3), uint8)

        if(interpolation_type == "nearest_neighbor"):
            for x in range(lenrow):
                for y in range(lencol):
                    ic = x - center_x
                    jc = y - center_y

                    rad =  math.sqrt(ic**2 + jc**2)

                    icd = (1/(1+k*rad))*ic
                    jcd = (1/(1+k*rad))*jc

                    i_d = icd + center_x
                    j_d = jcd + center_y

                    i_near = round(i_d)
                    j_near = round(j_d)

                    corrected_image[x, y] = distorted_image[i_near, j_near]

        if(interpolation_type == "bilinear"):
            for x in range(lenrow):
                for y in range(lencol):
                    ic = x - center_x
                    jc = y - center_y

                    rad = math.sqrt(ic**2 + jc**2)

                    icd = (1/(1+k*rad))*ic
                    jcd = (1/(1+k*rad))*jc

                    i_d = icd + center_x
                    j_d = jcd + center_y

                    x1 = math.floor(i_d)
                    x2 = math.ceil(i_d)
                    y1 = math.floor(j_d)
                    y2 = math.ceil(j_d)

                    if((y1 != y2) and (x1 != x2)):
                        p1 = [x1, y1, distorted_image[x1, y1]]
                        p2 = [x1, y2, distorted_image[x1, y2]]
                        p3 = [x2, y1, distorted_image[x2, y1]]
                        p4 = [x2, y2, distorted_image[x2, y2]]
                        intensity = interpolation()
                        corrected_image[x, y] = intensity.bilinear_interpolation(p1, p2, p3, p4, i_d, j_d)

                    else:
                        corrected_image[x, y] = distorted_image[round(i_d), round(j_d)]

        return corrected_image
