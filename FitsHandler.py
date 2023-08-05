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

    def plot_histogram_of_region(self, region):
        x1, y1, x2, y2 = region
        region_data = self.fits_image[y1:y2, x1:x2]
        plot_file(region_data)
        plt.figure()
        plt.hist(region_data.flatten(), bins=100, color='b', range=[1, 20000])
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of the Region')
        plt.grid(True)
        plt.show()
