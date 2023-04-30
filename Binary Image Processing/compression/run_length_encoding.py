from pickletools import uint8
from dip import *

class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """

        lenrow, lencol = binary_image.shape

        run_length = []
        c = 1

        reference = binary_image[0, 0]#append reference to run_length
        run_length.append(reference)

        for x in range(lenrow):
            for y in range(lencol):
                if y == lencol - 1 and x != lenrow - 1:
                    if(binary_image[x, y] == binary_image[x+1, 0]):
                        c += 1
                    else:
                        run_length.append(c)
                        c = 1
                elif y == lencol - 1 and x == lenrow - 1:
                    run_length.append(c)
                else:
                   if binary_image[x, y] == binary_image[x, y+1]:
                        c += 1
                   else:
                        run_length.append(c)
                        c = 1
                


        return run_length  # replace zeros with rle_code

    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """


        """
        image = zeros((width, height), dtype = uint8)

        default_color = rle_code[0]
        print(default_color)"""

        default_value = rle_code[0]
        temp = []

        for x in range(1, len(rle_code)):
            if default_value == 0:
                temp.extend(zeros(rle_code[x]))
                default_value = 255

            elif default_value == 255:
                temp.extend((255 * ones(rle_code[x])))
                default_value = 0

        image = array(temp).reshape(height, width) 
        return  image  # replace zeros with image reconstructed from rle_Code





        




