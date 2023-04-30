from dip import *
import math
class Coloring:

    def intensity_slicing(self, image, n_slices):
        '''
       Convert greyscale image to color image using color slicing technique.
       takes as input:
       image: the grayscale input image
       n_slices: number of slices
        
       Steps:
 
        1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        2. Randomly assign a color to each interval
        3. Create and output color image
        4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
 
       returns colored image
       '''
        color_image = zeros((image.shape[0], image.shape[1], 3), dtype = uint8)
        interval = int(image.max()/n_slices)
        list_interval = [0]
        for x in range(n_slices):
            list_interval.append(interval + (interval*x))
        colors = random.randint(0, 255, (n_slices, 3))

        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                for z in range(n_slices-1):
                    if image[x,y] <= list_interval[z+1]:
                        color_image[x][y] = colors[z]
                        break


        return color_image

    def color_transformation(self, image, n_slices, theta):
        '''
        Convert greyscale image to color image using color transformation technique.
        takes as input:
        image:  grayscale input image
        colors: color array containing RGB values
        theta: (phase_red, phase,_green, phase_blue) a tuple with phase values for (r, g, b) 
        Steps:
  
         1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
         2. create red values for each slice using 255*sin(slice + theta[0])
            similarly create green and blue using 255*sin(slice + theta[1]), 255*sin(slice + theta[2])
         3. Create and output color image
         4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
  
        returns colored image
        '''
        interval = []
        r = []
        g = []
        b = []

        for x in range(n_slices):
            interval.append(x * (255/n_slices))
            r.append(abs(255 * math.sin(x + theta[0])))
            g.append(abs(255 * math.sin(x + theta[1])))
            b.append(abs(255 * math.sin(x + theta[2])))
        interval.append(float(255))

        color_image = zeros((image.shape[0], image.shape[1], 3), dtype = uint8)

        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                for z in range(1, n_slices):
                    if interval[z] <= image[x, y] and image[x, y] < interval[z + 1]:
                        color_image[x][y][0] = r[z]
                        color_image[x][y][1] = g[z]
                        color_image[x][y][2] = b[z]
                        break

        return color_image



        

