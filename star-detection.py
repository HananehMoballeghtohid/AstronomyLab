import os
from FitsHandler import FitsHandler
from StarFinder import StarFinder


def main():

    # reading data and plotting it:
    FITS_PATH = os.getcwd() + "/data/stars.fits"
    fits_file = FitsHandler(FITS_PATH)
    fits_image = fits_file.get_file()
    fits_file.plot_file()

    # detecting stars using photutils:
    star_finder = StarFinder(60000, 15, fits_image)
    star_finder.print_detected_coordinates()
    star_finder.plot_detected_coordinates()


if __name__ == '__main__':
    main()
