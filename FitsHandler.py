import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt


def plot_file(image: np.ndarray):
    print("plotting fits file...")
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.show()


class FitsHandler:

    def __init__(self, fits_path: str):
        self.fits_path: str = fits_path
        print("reading fits file...")
        hdu_list = fits.open(self.fits_path)
        fits_image = hdu_list[0].data
        hdu_list.close()
        self.fits_image: np.ndarray = fits_image

    def get_file(self) -> np.ndarray:
        return self.fits_image

    def plot_file(self):
        print("plotting fits file...")
        plt.figure()
        plt.imshow(self.fits_image, cmap='gray')
        plt.show()
