import os
from astropy.io import fits
import matplotlib.pyplot as plt
from photutils import DAOStarFinder


def main():
    # importing fits image and converting it to grayscale:
    print("opening fits file...")
    FITS_PATH = os.getcwd() + "/data/stars.fits"
    hdu_list = fits.open(FITS_PATH)
    fits_image = hdu_list[0].data
    hdu_list.close()

    # plotting the image:
    print("plotting fits file...")
    plt.figure()
    plt.imshow(fits_image, cmap='gray')
    plt.show()

    # detecting stars using photutils:
    star_finder = DAOStarFinder(threshold=60000, fwhm=15)
    detected_stars = star_finder(fits_image)
    x_coordinates = detected_stars['xcentroid']
    y_coordinates = detected_stars['ycentroid']
    print("Detected stars (x, y):")
    for x, y in zip(x_coordinates, y_coordinates):
        print(f"({x}, {y})")

    # plotting detected stars on the original image to check the result:
    plt.imshow(fits_image, cmap='gray', origin='lower')
    plt.scatter(x_coordinates, y_coordinates, marker='o', s=1, color='red')
    plt.xlabel('X pixel coordinate')
    plt.ylabel('Y pixel coordinate')
    plt.title('Detected Stars on Original FITS Image')

    # Show the plot
    plt.show()


if __name__ == '__main__':
    main()
