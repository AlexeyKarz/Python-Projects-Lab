import numpy as np


def invert_colors(image):
    """
    Invert the colors of an image
    :param image: the input image
    :return: the inverted image
    """
    return 1 - image


def rgb_to_grayscale(image):
    """
    Convert an RGB image to a grayscale image using the standard formula
    :param image: the input image
    :return: the grayscale image
    """

    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError('The input image must have 3 color channels (RGB)')

    # extract the color channels
    R, G, B = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    # convert to grayscale using the formula
    grayscale = 0.2989 * R + 0.5870 * G + 0.1140 * B

    return grayscale.astype(np.uint8)


def resize_image(image, factor):
    """
    Resize an image by a given factor using averaging
    :param image: the input image (numpy.ndarray)
    :param factor: the factor by which to reduce the size (int)
    :return: the resized image
    """
    if factor < 1:
        raise ValueError("Factor must be an integer greater than or equal to 1.")

        # Calculate the size of the blocks to average
    block_size = factor

    # Calculate the new image size
    new_height = image.shape[0] // block_size
    new_width = image.shape[1] // block_size

    # Prepare an empty array for the resized image
    resized_image = np.zeros((new_height, new_width, image.shape[2]), dtype=np.uint8)

    for y in range(new_height):
        for x in range(new_width):
            for c in range(image.shape[2]):
                # Calculate the average of the block
                block = image[y * block_size:(y + 1) * block_size, x * block_size:(x + 1) * block_size, c]
                block_average = np.mean(block, axis=(0, 1))
                resized_image[y, x, c] = block_average

    return resized_image