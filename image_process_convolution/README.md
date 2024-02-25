# Image Processing Utilities

The initial goal of this project is to experiment with different image procesing techniques, especially on how to apply convolution for working with images. This repository contains a collection of Python modules designed for basic image processing tasks. These utilities demonstrate fundamental operations such as convolution-based filtering, image transformations, and the application of various image effects without relying on external image processing libraries.

*NOTE: Most of the functions are written as an educational project. If you aim for practical applications, consider using image processing libraries like OpenCV, PIL/Pillow, or SciPy which have similar functionality and are more efficient.*

## Modules

### 1. `convfunc.py`
This module provides functions related to the convolution operation, a cornerstone in image processing for applying filters like blurring, embossing, and edge detection.
-  **generate_gaussian_kernel(size, sigma=1)**: Generate a square Gaussian kernel
-  **gaussian_blur(image, kernel)**: Apply Gaussian blur to an image using a given kernel
-  **high_pass_filter(image, kernel)**: Apply a high pass filter to an image using a given kernel
-  **emboss_filter_kernel(direction='TL')**: Create a 3x3 emboss filter kernel based on the given light direction
-  **conv2d(image, kernel)**: Apply a 2D convolution to an image using a given kernel
-  **apply_emboss(image, kernel)**: Apply an emboss filter to an image using a given kernel

### 2. `imtransform.py`
Focused on image transformations, this module includes functions for resizing and applying various artistic effects to images.
- **invert_colors(image)**: Invert the colors of an image
- **rgb_to_grayscale(image)**: Convert an RGB image to a grayscale image using the standard formula
- **resize_image(image, factor)**: Resize an image by a given factor using averaging

### 3. `main.py`
Serves as an entry point to demonstrate the usage of functions defined in the convfunc.py and imtransform.py modules.


## Extending the Library

Contributions to extend the functionality of these utilities are welcome. Ideas for further development include:

- Implementing additional convolution-based filters (e.g., Sobel edge detection, Laplacian filters).
- Introducing more complex image effects (e.g. sketch effects).
- Optimizing existing functions for performance improvements.

### License

This project is open-sourced under the MIT License.
