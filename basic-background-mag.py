import os

from FitsHandler import FitsHandler


def main():
    # Assuming we have already selected regions with no stars,
    # We draw histograms of our selected regions to see which one is better:

    FITS_PATH = os.getcwd() + "/data/stars.fits"
    fits_file = FitsHandler(FITS_PATH)
    region = [475, 575, 650, 750]
    fits_file.plot_histogram_of_region(region)

    # then we need to calculate the total flux of the background
    # and calculate magnitude comparing to the star


if __name__ == '__main__':
    main()
