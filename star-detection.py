import os
from FitsHandler import FitsHandler
from StarFinder import StarFinder

"""
Author: Hananeh Moballeghtohid
"""


def main():
    # reading data and plotting it:
    FITS_PATH = os.getcwd() + "/data/stars.fits"
    focal_length = 1
    pixel_size = 4.30 * 1e-6
    fits_file = FitsHandler(FITS_PATH, focal_length, pixel_size)
    fits_image = fits_file.get_file()
    fits_file.plot_file()

    # detecting stars using photutils:
    star_finder = StarFinder(40000, 10, fits_image)
    star_finder.print_detected_coordinates()
    star_finder.plot_detected_coordinates()


if __name__ == '__main__':
    main()
