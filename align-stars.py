import astroalign
from astropy.io import fits

from FitsHandler import FitsHandler
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    NUMBER_OF_FILES = 23
    science_images = []
    aligned_images = []

    fits_path = "".join([os.getcwd() + "/data/1.fits"])
    target_image = FitsHandler(fits_path, 0, 0).get_filtered()
    aligned_images.append(target_image)
    science_images.append(target_image)
    plt.subplot(1, 2, 1)
    plt.imshow(science_images)
    plt.title('Target Image')

    # make all science images match pixel to pixel to target:
    for i in range(NUMBER_OF_FILES - 1):
        fits_path = "".join([os.getcwd() + "/data/", f"{i+2}.fits"])
        science_image = FitsHandler(fits_path, 0, 0).get_filtered()
        science_images.append(science_image)
        aligned_image, footprint = astroalign.register(science_image, target_image)
        aligned_images.append(aligned_image)

    master_science = np.sum(aligned_images, axis=0)
    plt.subplot(1, 2, 2)
    plt.imshow(master_science)
    plt.title('Master Image')
    plt.show()

    hdu = fits.PrimaryHDU(master_science)
    hdu.writeto('x-h-perseus-20s-ISO1600-6inch-Newtonian-B-Aznaveh-19th-July-2023-Hemmati-Maleki-Mobalegh.fits')


if __name__ == '__main__':
    main()
