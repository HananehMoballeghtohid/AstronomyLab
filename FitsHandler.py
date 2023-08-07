import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from numpy import ndarray


def plot_file(image: np.ndarray):
    print("plotting fits file...")
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.show()


class FitsHandler:

    def __init__(self, fits_path: str, focal_length: int, pixel_size: float):
        self.fits_path: str = fits_path
        print("reading fits file...")
        hdu_list = fits.open(self.fits_path)
        fits_image = hdu_list[0].data
        hdu_list.close()
        self.fits_image: np.ndarray = fits_image
        self.focal_length: int = focal_length
        self.pixel_size: float = pixel_size

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

    def calculate_flux_of_region(self, region) -> float:
        x1, y1, x2, y2 = region
        sum_flux = 0
        for i in range(y1, y2):
            for j in range(x1, x2):
                sum_flux += self.fits_image[i, j]
        return sum_flux

    def calculate_mean_pixel_flux(self, region) -> ndarray:
        x1, y1, x2, y2 = region
        region_data = self.fits_image[y1:y2, x1:x2]
        return np.mean(region_data)

    def find_darkest_area(self, size):
        height, width = self.fits_image.shape
        darkest_area_x = 0
        darkest_area_y = 0
        min_average_value = np.inf

        for y in range(height - size + 1):
            for x in range(width - size + 1):
                window_data = self.fits_image[y:y + size, x:x + size]
                average_value = np.mean(window_data)

                # Update the darkest area if a new minimum average value is found
                if average_value < min_average_value:
                    min_average_value = average_value
                    darkest_area_x = x
                    darkest_area_y = y

        return darkest_area_x, darkest_area_y, min_average_value

    def get_pixel_scale_by_arcsecond(self) -> float:
        return (206265*self.pixel_size)/self.focal_length

    def draw_red_box(self, region):
        print("drawing red box around region...")
        plt.imshow(self.fits_image, cmap='gray')
        rect = Rectangle((region[0], region[1]), region[2] - region[0], region[3] - region[1],
                         linewidth=2, edgecolor='r', facecolor='none')
        plt.gca().add_patch(rect)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Image with Red Box Around Selected Region')
        plt.show()
