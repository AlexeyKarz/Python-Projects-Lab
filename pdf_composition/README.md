# PDF Processing Tools

This repository contains scripts I wrote to meet my personal needs for processing PDF files.

## 1. PDF composition
Scripts combining (n-up) PDF pages into a single file and merging multiple PDF files into one. These tools are useful for managing lecture notes, presentations, and other document types that require consolidation or reorganization.
*(If you have not many files, I would also suggest you to try using operating systems print dialog, that allows to n-up pages into one and save as new pdf file.)*

*NOTE: All the position indexes and canvas sizes can be changed according to your goals and needs*



---
### Below is Legacy Code. My best implementation of NUP in python so far is here: [nup_pikepdf](https://github.com/AlexeyKarz/Python-Projects-Lab/tree/main/pdf_composition/nup_pikepdf). 
---

### 1.1 `functions.py`
Prerequisites for `functions.py` are: Python 3.x, PyMuPDF (fitz), PyPDF2, 
Ensure you have Python installed on your system. You can download it from python.org.

NOTE: The n-up function first transofrms pdf pages into images and then inserts them into the created page (6 pages into 1 page). This leads to inability to select text and significant file size. If this is a problem, look **1.2 `pikepdf_pdf_nup.ipynb`**

Usage of `functions.py`:

- Combining PDF Pages
To combine multiple pages from a single PDF into a new file with pages arranged in a grid layout:

```
from your_script_name import combine_pdf_pages

input_pdf_path = "path/to/your/input.pdf"
output_pdf_path = "path/to/your/output_combined.pdf"

combine_pdf_pages(input_pdf_path, output_pdf_path)
```
The sample page of the resulting file (the original file is the free presentation taken from [Canva](https://www.canva.com))):
<img width="544" alt="image" src="https://github.com/AlexeyKarz/Python-Projects-Lab/assets/92441134/f1365ae9-4d05-4e67-a872-60f038d76ade">



- Merging Multiple PDF Files
To merge all PDF files from a specified directory into a single PDF file:

```
from your_script_name import combine_pdf_files

input_directory = "path/to/your/pdf/directory"
output_file = "path/to/your/merged_output.pdf"

combine_pdf_files(input_directory, output_file)
```

- Processing a Directory of PDFs. To process an entire directory of PDF files, combining the pages of each into new files in a specified output directory:

```
from your_script_name import process_pdf_directory

source_directory = "path/to/your/source/directory"
output_directory = "path/to/your/output/directory"

process_pdf_directory(source_directory, output_directory)
```

Make sure to replace your_script_name with the actual name of your Python script file if you've encapsulated the functionality into a specific module. Adjust the paths to reflect the actual usage scenarios and file locations relevant to your project.

### 1.2 `pikepdf_pdf_nup.ipynb`

This Jupyter notebook was written to face the problem with inability to select the text. I found out that for my purpose of compositing pdf pages the best python library is [pikepdf](https://github.com/pikepdf/pikepdf). Using its functionality I wrote the code that allows to n-up 9 pages into 1, saving the opportunity to select the text.

NOTE: For now the code of `pikepdf_pdf_nup.ipynb` allows to n-up only 9 pages per page. Later I plan to add variety to chose between 2, 4, 6, 9, 12 pages. But feel free to modify the code according to your goals.

The sample page of the resulting file (the original file is the free presentation taken from [Canva](https://www.canva.com)):
<img width="870" alt="image" src="https://github.com/AlexeyKarz/Python-Projects-Lab/assets/92441134/b4d3c4e2-0c87-4294-af75-c9393c918490">


Contributions are welcome! If you have suggestions for improvements or bug fixes, please open an issue.

#### MIT License

