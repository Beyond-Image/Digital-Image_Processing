from dip import *
import math
class Filtering:

    def __init__(self, image, filter_name, filter_size, var = None):
        """initializes the variables of spatial filtering on an input image
        takes as input:
        image: the noisy input image
        filter_name: the name of the filter to use
        filter_size: integer value of the size of the fitler
        
        """

        self.image = image

        if filter_name == 'arithmetic_mean':
            self.filter = self.get_arithmetic_mean
        elif filter_name == 'geometric_mean':
            self.filter = self.get_geometric_mean
        if filter_name == 'local_noise':
            self.filter = self.get_local_noise
        elif filter_name == 'median':
            self.filter = self.get_median
        elif filter_name == 'adaptive_median':
            self.filter = self.get_adaptive_median

        self.filter_size = filter_size
        
        # global_var: noise variance to be used in the Local noise reduction filter        
        self.global_var = var
        
        # S_max: Maximum allowed size of the window that is used in adaptive median filter
        self.S_max = 15

    def get_arithmetic_mean(self, roi):
        """Computes the arithmetic mean of the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the arithmetic mean value of the roi"""
        mean = 0

        for x in range(len(roi)):
            mean += roi[x]
        mean = mean/len(roi)
        
        return mean

    def get_geometric_mean(self, roi):
        """Computes the geometric mean for the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the geometric mean value of the roi"""
        mean = 1
        for x in range(len(roi)):
            mean *= roi[x]

        mean = math.pow(mean, 1/len(roi))
        
        return mean

    def get_local_noise(self, roi):
        """Computes the local noise reduction value
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the local noise reduction value of the roi"""
        
        local_mean = sum(roi)/ len(roi)
        n = len(roi)

        loc_var = 0
        for x in roi:
            loc_var += (x-local_mean)**2

        loc_var /= (n)

        if loc_var == 0:
            return local_mean

        value = 0
        middle = n//2
        mean = roi[middle] - local_mean
        value = (1/loc_var) * mean

        return value


    def get_median(self, roi):
        """Computes the median for the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the median value of the roi"""
        sorted_array = sorted(roi)
        length = len(sorted_array)
        mid = length//2

        if(length%2 == 0):
            median = (sorted_array[mid-1] + sorted_array[mid])/2
        else:
            median = sorted_array[mid]
        
        return median


    def get_new_roi(self, pad_image, window_size, currRow, currCol):
        roi = []
        padded_size = window_size//2

        for x in range(window_size):
            for y in range(window_size):
                roi.append(pad_image[currRow - padded_size + x][currCol - padded_size + y])


        return roi

    def get_adaptive_median(self, pad_image, roi, window_size, currRow, currCol):
        """Use this function to implment the adaptive median.
        It is left up to the student to define the input to this function and call it as needed. Feel free to create
        additional functions as needed.
        """
        z_min = min(roi)
        z_max = max(roi)

        sorted_array = sorted(roi)
        length = len(sorted_array)
        mid = length//2
        if(length%2 == 0):
            median = (sorted_array[mid-1] + sorted_array[mid])/2
        else:
            median = sorted_array[mid]
        z_median = median

        A1 = z_median - z_min
        A2 = z_median - z_max
        if(A1 > 0 and A2 < 0):
            B1 = pad_image[currRow][currCol] - z_min
            B2 = pad_image[currRow][currCol] - z_max
            if(B1 > 0 and B2 < 0):
                return pad_image[currRow][currCol]
            else:
                return z_median
        else:
            window_size += 1
            if(window_size <= 15):
                roi = self.get_new_roi(pad_image, window_size, currRow, currCol)
                return self.get_adaptive_median(pad_image, roi, window_size, currRow, currCol)
            else:
                return z_median

        

    def filtering(self):
        """performs filtering on an image containing gaussian or salt & pepper noise
        returns the denoised image
        ----------------------------------------------------------
        Note: Here when we perform filtering we are not doing convolution.
        For every pixel in the image, we select a neighborhood of values defined by the kernal and apply a mathematical
        operation for all the elements with in the kernel. For example, mean, median and etc.

        Steps:
        1. add the necesssary zero padding to the noisy image, that way we have sufficient values to perform the operati
        ons on the pixels at the image corners. The number of rows and columns of zero padding is defined by the kernel size
        2. Iterate through the image and every pixel (i,j) gather the neighbors defined by the kernel into a list (or any data structure)
        3. Pass these values to one of the filters that will compute the necessary mathematical operations (mean, median, etc.)
        4. Save the results at (i,j) in the ouput image.
        5. return the output image

        Note: You can create extra functions as needed. For example if you feel that it is easier to create a new function for
        the adaptive median filter as it has two stages, you are welcome to do that.
        For the adaptive median filter assume that S_max (maximum allowed size of the window) is 15
        """
        if(self.filter == self.get_local_noise):
            padding_size = self.filter_size//2 
            pad_img = zeros((self.image.shape[0] + (2*padding_size), self.image.shape[1] + (2*padding_size)))
            pad_img[padding_size:-padding_size, padding_size:-padding_size] = self.image

            final_image = zeros((self.image.shape[0], self.image.shape[1]))
            mean = sum(self.image)/len(self.image)

            for i in range(padding_size, pad_img.shape[0] - padding_size):
                for j in range(padding_size, pad_img.shape[0]-padding_size):
                    roi = []
                    for x in range(self.filter_size):
                        for y in range(self.filter_size):
                            roi.append(pad_img[i-padding_size + x][j - padding_size + y])
                    mean = self.filter(roi)
                    gxy = pad_img[i][j]
                    mean = gxy - self.global_var * mean
                    final_image[i-padding_size][j-padding_size] = mean

            return final_image
        

        if(self.filter == self.get_adaptive_median):

            "add more padding for max window size"
            padding_size = 15//2 
            pad_img = zeros((self.image.shape[0] + (2*padding_size), self.image.shape[1] + (2*padding_size)))
            pad_img[padding_size:-padding_size, padding_size:-padding_size] = self.image

            window_size = self.filter_size 

            final_image = zeros((self.image.shape[0], self.image.shape[1]))
            for i in range(padding_size, pad_img.shape[0] - padding_size):
                for j in range(padding_size, pad_img.shape[1] - padding_size):
                    z_xy = pad_img[i][j]
                    roi = []
                    for x in range(window_size):
                        for y in range(window_size):
                            roi.append(pad_img[i - window_size + x][j - window_size + y])
                    final_image[i - padding_size][j - padding_size] = self.filter(pad_img, roi, window_size, i, j)



            return final_image
        

        else:
            final_image = zeros((self.image.shape[0], self.image.shape[1]))
            padding_size = self.filter_size//2
            pad_img = zeros((self.image.shape[0] + (2*padding_size), self.image.shape[1] + (2*padding_size)))
            pad_img[padding_size:-padding_size, padding_size:-padding_size] = self.image

            for i in range(padding_size, pad_img.shape[0] - padding_size):
                for j in range(padding_size, pad_img.shape[1] - padding_size):
                    roi = []
                    for x in range(self.filter_size):
                        for y in range(self.filter_size):
                            roi.append(pad_img[i - padding_size + x][j - padding_size + y])
                    mean = self.filter(roi)
                    final_image[i - padding_size][j - padding_size] = mean
            return final_image

