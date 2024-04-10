# Project Title

This is a Python project that provides a function `nup_pdf` for combining multiple pages of a PDF into one page. The function supports combining 2, 3, 4, 6, 9, or 12 pages into one. This is useful for printing multiple slides of a presentation on one page for studies, creating cheat sheets and other purposes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. The project also depends on the `pikepdf` library. You can install it using pip:

```bash
pip install pikepdf
```

### Installing

You can either copy the `func.py` file to your project and use the functions as needed, or you can clone the entire directory to your machine. Since this repository consists of many projects, you don't need to clone the entire repository. You can clone only the `main.py`, `func.py` scripts, `sample.pdf` (it you want to run unit tests, or have your own file with the sama name) and `tests` directory.


## Usage

The main function of this project is `nup_pdf(input_pdf, output_pdf, slides_per_page)`. Here is how you can use it:

```python
from func import nup_pdf

# define the number of slides per page (possible values are 2, 4, 6, 9, 12)
slides_per_page = 9
# define the path of the input pdf
pdf_path = "sample.pdf"
# define the path of the output pdf
output_path = f"{pdf_path.strip('.pdf')}_{slides_per_page}_combined.pdf"
# run the nup function
nup_pdf(pdf_path, output_path, slides_per_page)
```

## Running the tests

The tests for this project are located in the `tests` directory. You can run them using the `test_runner.py` script:

```bash
python tests/test_runner.py
```
*NOTE: You need to have the `sample.pdf` file in the root directory of the project to run the tests.*
## Contributing

Feel free to contribute to this project. You can add new features, improve the existing ones, or fix bugs. If you want to contribute, please open an issue or a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

* Thanks to the `pikepdf` library for making PDF manipulation in Python easy.
* Thanks to all the contributors who participate in this project.