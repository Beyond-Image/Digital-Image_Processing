import math
import dip
from dip import *



class ShapeCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Implement the blob coloring algorithm
        takes as input:
        image: binary image
        return: a list/dict of regions
        """

        regions = dict()

        

        lenrow, lencol = image.shape
        new_regions = zeros((lenrow, lencol), dtype = int)


        k = 1

        for x in range(lenrow):
            for y in range(lencol):
                if image[x, y] == 255 and image[x, y-1] == 0 and image[x-1, y] == 0:
                    new_regions[x, y] = k
                    regions[k] = [(x, y)] 
                    k += 1
                elif image[x, y] == 255 and image[x, y-1] == 0 and image[x-1, y] == 255:
                    new_regions[x, y] = new_regions[x-1, y] 
                    regions[new_regions[x-1, y]].append((x, y))
                elif image[x, y] == 255 and image[x, y-1] == 255 and image[x-1, y] == 0:
                    new_regions[x, y] = new_regions[x, y-1]
                    regions[new_regions[x, y-1]].append((x, y)) 
                elif image[x, y] == 255 and image[x, y] == 255 and image[x, y] == 255:
                    new_regions[x, y] = new_regions[x-1, y] 
                    regions[new_regions[x-1, y]].append((x, y)) 
                    if new_regions[x, y-1] != new_regions[x-1, y]:
                        regions[new_regions[x-1, y]].extend(regions[new_regions[x, y-1]])
                        regions[new_regions[x, y-1]] = []


        print("\nNumber of regions: ", len(regions))

        return regions

    def identify_shapes(self, region):
        """Compute shape features area and centroid, and shape
        Ignore shapes smaller than 10 pixels in area.
        takes as input
        region: a list/dict of pixels in a region
        returns: shapes, a data structure with centroid, area, and shape (c, s, r, or e) for each region
        c - circle, s - squares, r - rectangle, and e - ellipse
        """


        # Please print your shape statistics to stdout, one line for each shape
        # Region: <region_no>, centroid: <centroid>, area: <shape area>, shape: <shape type>
        # Example: Region: 871, centroid: (969.11, 51.11), area: 707, shape: c



        shapes = dict()
        for key, value in list(region.items()):

            if len(value) < 10:
                continue

            area = len(value)


            Xc = (1/area) * sum(x[1] for x in value)
            Yc = (1/area) * sum(x[0] for x in value)
            centroid = (Xc, Yc)


            width = max([x[1] for x in value]) - min([x[1] for x in value])
            height = max([x[0] for x in value]) - min([x[0] for x in value])

            threshold = 0.065 * (width + height)/2

            if abs(width - height) <= threshold:
                if abs(width - 2 * math.sqrt(area/math.pi)) <= threshold:
                    shape = 'c'
                else:
                    shape = 's'
            else:
                area_delta = abs(height * width - area)
                if area_delta <= 0.065 * (width*height):
                    shape = 'r'
                else:
                    shape = 'e'





            shapes[key] = {'Region':key, 'Centroid':centroid, 'Area':area, 'shape':shape}
            #print("Region: ", count, "Centroid", centroid, "Area: ", area)
            print("Region: ", key, "Centroid", centroid, "Area: ", area, "Shape: ", shape)

        return shapes

    def count_shapes(self, shapes_data):
        """Compute the count of shapes using the shapes data returned from identify shapes function
           takes as input
           shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
           returns: a dictionary with count of each shape
           Example return value: {'circles': 21, 'ellipses': 25, 'rectangles': 31, 'squares': 23}
           """

        circles = 0
        squares = 0
        ellipses = 0
        rectangles = 0

        for key, value in shapes_data.items():
            if value['shape'] == 'c':
                circles += 1
            elif value['shape'] == 'e':
                ellipses += 1
            elif value['shape'] == 'r':
                rectangles += 1
            elif value['shape'] == 's':
                squares += 1

        return {"circles": circles, "ellipses": ellipses, "rectangles": rectangles, "squares": squares}

    def mark_image_regions(self, image, shapes_data):
        """Creates a new image with computed stats for each shape
        Make a copy of the image on which you can write text.
        takes as input
        image: binary image
        shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
        returns: image marked with center and shape_type"""

        new_image = image.copy()

        for key, value in shapes_data.items():
            dip.putText(new_image, value['shape'], (int(value['Centroid'][0]), int(value['Centroid'][1])), dip.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)

        return new_image

