import os

import numpy as np

from FitsHandler import FitsHandler


def main():
    # importing fits file:
    fits_path = os.getcwd() + "/data/stars.fits"

    # 1m telescope and canon 1200D camera:
    focal_length = 1
    pixel_size = 4.30 * 1e-6
    fits_file = FitsHandler(fits_path, focal_length, pixel_size)

    # calculating pixel scale
    pixel_scale = fits_file.get_pixel_scale_by_arcsecond()
    print("Pixel scale: {:.2f} arcseconds/pixel".format(pixel_scale))

    # finding the darkest area and its mean pixel flux and std:
    darkest_area_x, darkest_area_y, pixel_mean_flux, flux_std = fits_file.find_darkest_area(100)
    print('The darkest area in the file starts at:', darkest_area_x, ',', darkest_area_y)
    print('The average pixel flux in the area is:', pixel_mean_flux)

    # plotting histogram:
    region = [darkest_area_x, darkest_area_y,
              darkest_area_x + 100,
              darkest_area_y + 100]
    fits_file.plot_histogram_of_region(region)

    # calculating flux by arcseconds squared
    arc_square_mean_flux = pixel_mean_flux / (pixel_scale ** 2)
    print("mean flux in one arcseconds squared: {:.2f} flux/arcsecond^2".format(arc_square_mean_flux))

    # calculating magnitude
    reference_mag = 8.88
    reference_flux = 28535.57
    magnitude = reference_mag - 2.5 * np.log10(arc_square_mean_flux / reference_flux)
    print("magnitude of background sky: {:.2f} mag/arcsecond^2".format(magnitude))


if __name__ == '__main__':
    main()
