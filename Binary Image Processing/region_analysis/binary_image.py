class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = [0]*256
        m=0
        lencol = len(image[0])
        lenrow = len(image)
        for x in range(lenrow):
            for y in range(lencol):
                scale = image[x][y]
                hist[scale] += 1
        return hist

    def find_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold assuming that the input histogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value
        Note: Use the iterative method to calculate the histogram. Do not use the Otsu's method
        Write your code to compute the optimal threshold method.
        This should be implemented using the iterative algorithm discussed in class (See Week 4, Lecture 7, slide 42
        on teams). Do not implement the Otsu's thresholding method. No points are awarded for Otsu's method.
        """

        threshold = len(hist)/2
        curr_mean1, curr_mean2 = 0, 0
        prev_mean1, prev_mean2 = 0, 0

        while True:
            curr_mean1, curr_mean2 = 0, 0
            num_pixels1, num_pixels2 = 0, 0
            for x in range(len(hist)):
                if( x < threshold):
                    curr_mean1 += hist[x] * x
                    num_pixels1 += hist[x]
                else:
                    curr_mean2 += hist[x] * x
                    num_pixels2 += hist[x]
            curr_mean1 /= num_pixels1
            curr_mean2 /= num_pixels2
            threshold = int((curr_mean1 + curr_mean2)/2)
            if(((curr_mean1 - prev_mean1) == 0) and ((curr_mean2 - prev_mean2) == 0)):
                break
            else:
                prev_mean1 = curr_mean1
                prev_mean2 = curr_mean2

        return threshold

    def binarize(self, image, threshold):
        """Comptues the binary image of the input image based on histogram analysis and thresholding
        takes as input
        image: a grey scale image
        threshold: to binarize the greyscale image
        returns: a binary image"""


        bin_img = image.copy()

        lenrow = len(image)
        lencol = len(image[0])

        for x in range(lenrow):
            for y in range(lencol): 
                if(bin_img[x][y] < threshold):
                    bin_img[x][y] = 0
                else:
                    bin_img[x][y] = 255

        return bin_img


