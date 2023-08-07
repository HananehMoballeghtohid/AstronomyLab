import numpy as np
from matplotlib import pyplot as plt
from photutils.detection import DAOStarFinder

"""
Author: Hananeh Moballeghtohid
"""


class StarFinder:
    def __init__(self, threshold: int, fwhm: int, star_image: np.ndarray):
        self.threshold: int = threshold
        self.fwhm: int = fwhm
        self.star_image: np.ndarray = star_image
        print("detecting stars...")
        star_finder = DAOStarFinder(self.threshold, self.fwhm)
        detected_stars = star_finder(self.star_image)
        self.x_coordinates = detected_stars['xcentroid']
        self.y_coordinates = detected_stars['ycentroid']

    def print_detected_coordinates(self):
        print("Detected stars (x, y):")
        for x, y in zip(self.x_coordinates, self.y_coordinates):
            print(f"({x}, {y})")

    def plot_detected_coordinates(self):
        plt.imshow(self.star_image, cmap='gray', origin='lower')
        plt.scatter(self.x_coordinates, self.y_coordinates, marker='o', s=1, color='red')
        plt.xlabel('X pixel coordinate')
        plt.ylabel('Y pixel coordinate')
        plt.title('Detected Stars on Original FITS Image')
        plt.show()
