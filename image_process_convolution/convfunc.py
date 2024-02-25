import numpy as np


def generate_gaussian_kernel(size, sigma=1):
    """
    Generate a square Gaussian kernel
    :param size: the size of the kernel (odd number)
    :param sigma: the standard deviation of the Gaussian distribution
    :return: the Gaussian kernel
    """

    kernel = np.fromfunction(lambda x, y: (1 / (2 * np.pi * sigma ** 2)) * np.exp(
        -((x - (size - 1) / 2) ** 2 + (y - (size - 1) / 2) ** 2) / (2 * sigma ** 2)), (size, size))
    return kernel / np.sum(kernel)  # normalize the kernel


def gaussian_blur(image, kernel):
    """
    Apply Gaussian blur to an image using a given kernel
    :param image: the input image
    :param kernel: the Gaussian kernel
    :return: the blurred image
    """

    if image.ndim != 3:
        raise ValueError('The input image must be a 3D array')

    # get the size of the kernel and the image
    kernel_size = kernel.shape[0]
    pad_width = kernel_size // 2
    image_height, image_width, num_channels = image.shape

    # pad the image
    padded_image = np.pad(image, [(pad_width, pad_width), (pad_width, pad_width), (0, 0)],
                          mode='constant', constant_values=0)

    # create a new image to store the result
    blurred_image = np.zeros_like(image)

    # apply the kernel to each pixel in the image (Gaussian blur)
    # Apply the kernel to each pixel for each channel
    for c in range(num_channels):
        for y in range(image_height):
            for x in range(image_width):
                # Element-wise multiplication and sum
                blurred_image[y, x, c] = np.sum(kernel * padded_image[y:y + kernel_size, x:x + kernel_size, c])

    return blurred_image


def high_pass_filter(image, kernel):
    """
    Apply a high pass filter to an image using a given kernel
    :param image: the input image
    :param kernel: the gaussian kernel for blurring
    :return: the high-pass filtered image
    """
    # apply the gaussian blur to the image
    blurred_image = gaussian_blur(image, kernel)

    # subtract the blurred image from the original image
    high_pass_image = image - blurred_image

    # normalize the image to ensure it's within the valid range of pixel values
    high_pass_image = np.clip(high_pass_image + 128, 0, 255)

    return high_pass_image.astype(np.uint8)


def emboss_filter_kernel(direction='TL'):
    """
    Create a 3x3 emboss filter kernel based on the given light direction
    :param direction: the direction of the light (TL, TR, BL, BR:
                      top-left, top-right, bottom-left, bottom-right)
    :return: the emboss filter kernel
    """
    if direction not in ['TL', 'TR', 'BL', 'BR']:
        raise ValueError('Invalid direction. It must be either TL, TR, BL, or BR')
    elif direction == 'TL':
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])
    elif direction == 'TR':
        kernel = np.array([[0, -1, -2],
                           [1, 1, -1],
                           [2, 1, 0]])
    elif direction == 'BL':
        kernel = np.array([[0, 1, 2],
                           [-1, 1, 1],
                           [-2, -1, 0]])
    else:  # direction == 'BR'
        kernel = np.array([[2, 1, 0],
                           [1, 1, -1],
                           [0, -1, -2]])
    return kernel


def conv2d(image, kernel):
    """
    Apply a 2D convolution to an image using a given kernel
    :param image: input 2D image
    :param kernel: The convolution kernel
    :return: the convolved image
    """
    kernel = np.flipud(np.fliplr(kernel))  # Flip the kernel
    output = np.zeros_like(image)
    image_padded = np.pad(image, [(1, 1), (1, 1)], mode='constant', constant_values=0)
    for x in range(image.shape[1]):  # Loop over every pixel of the image
        for y in range(image.shape[0]):
            # Apply the kernel
            output[y, x] = (kernel * image_padded[y:y + 3, x:x + 3]).sum()
    return output


def apply_emboss(image, kernel):
    """
    Apply an emboss filter to an image using a given kernel
    :param image: input image
    :param kernel: the emboss filter kernel
    :return: the embossed image
    """
    if image.ndim != 3:
        raise ValueError("The input image must be a 3D array")

    # Convert image to a type that can handle overflow/underflow safely
    image_float = image.astype(np.float32)

    # Prepare the output image
    embossed_image = np.zeros_like(image_float)

    # Apply the kernel to each channel
    for c in range(image.shape[2]):
        embossed_image[:, :, c] = conv2d(image_float[:, :, c], kernel)

    # Normalize the result and ensure it's within the valid range of pixel values
    # Add 128 to recenter the values, and clip between 0 and 255
    embossed_image = np.clip(embossed_image, 0, 255)

    return embossed_image.astype(np.uint8)
