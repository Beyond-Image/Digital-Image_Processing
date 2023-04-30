"""dip_hw0.py: Starter file to run homework 0"""

__author__      = "Khadija Khaldi"
# revised by Zhenggang Li
#revised by Shishir Shah
__version__ = "1.0.1"

from dip import *
import sys
from image_op import operations


def display_image(window_name, image):
    """A function to display image"""
    namedWindow(window_name)
    imshow(window_name, image)
    waitKey(0)


def main():
    """ The main function that parses input arguments, calls the appropriate
     method and writes the output image"""

    #Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-ic", "--image-color", dest="image_l",
                        help="specify the name of the color image", metavar="IMAGELEFT")
    parser.add_argument("-ib", "--image-bw", dest="image_r",
                        help="specify the name of the black_white image", metavar="IMAGERIGHT")

    parser.add_argument("-c", "--column", dest="column",
                        help="specify column (c) for merging", metavar="COLUMN")


    parser.add_argument("-tc", "--target-color", dest="target_color", action='append',
                        help="specify the target color for color extraction", metavar="TARGETCOLOR")

    parser.add_argument('-t', '--threshold', dest='threshold',
                        help='specify the threshold for color extraction', metavar='THRESHOLD')

    args = parser.parse_args()

    # Load image
    if args.image_l is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        input_image_color = imread(args.image_l, 1)

    if args.image_r is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        input_image_bw = imread(args.image_r, 1)

    # Check the location to merge
    if args.column is None:
        print("Merging location Y is not specified using default (149)")
        print("use the -h option to see usage information")
        column = 149
    else:
        column = int(args.column)
        if not column in range(0, input_image_color.shape[1]):
            print("column value outside image bounds, value should be between 0 and %s" % (input_image_color.shape[1]))
            print("Using default value (149)")
            column = 149

    if args.target_color is None:
        print('Targeted Color not specified using default [0, 0, 255]')
        target_color = [0, 0, 255]
    else:
        target_color = [int(i) for i in args.target_color]
        for i in target_color:
            if i < 0 or i > 255:
                print("Intensity of each color channel should be between 0 and 255")
                print("Using default value (0, 0, 255)")
                target_color = [0, 0, 255]

    if args.threshold is None:
        print('Threshold is not specified using default (180)')
        threshold = 180    
    else:
        threshold = float(args.threshold)

    # Write output file
    outputDir = 'output/'
    operation_obj = operations.Operation()

    merged_image = operation_obj.merge(input_image_color, input_image_bw, column=column)
    output_image_name = outputDir + 'merged_image' + "_c_%s" % (column) + ".jpg"
    imwrite(output_image_name, merged_image)

    color_extracted_image =operation_obj.color_slicing(input_image_color, input_image_bw, target_color=target_color, threshold=threshold)
    output_image_name = outputDir + 'color_extracted_image_' + "_".join([str(k) for k in target_color]) + ".jpg"
    imwrite(output_image_name, color_extracted_image)


if __name__ == "__main__":
    main()







