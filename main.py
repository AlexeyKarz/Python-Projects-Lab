from convfunc import generate_gaussian_kernel, gaussian_blur, high_pass_filter, apply_emboss, emboss_filter_kernel
from imtransform import invert_colors, rgb_to_grayscale, resize_image
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # read the image
    image_path = "dog.jpg"
    image = plt.imread(image_path)
    # Resize the image if necessary (optional)
    # resized_image = resize_image(image, 6)

    # generate a Gaussian kernel
    kernel_size = 15  # the size of the kernel (5x5)
    sigma = 3  # the standard deviation of the Gaussian distribution
    kernel = generate_gaussian_kernel(kernel_size, sigma=sigma)

    # apply Gaussian blur to the image
    blurred_image = gaussian_blur(image, kernel)

    # display the original and the blurred image
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(blurred_image)
    plt.title('Blurred Image')
    plt.axis('off')

    plt.show()

    # save the blurred image if needed
    # plt.imsave('image_blurred.png', blurred_image)

