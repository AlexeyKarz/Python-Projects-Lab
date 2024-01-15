# Flatmates Bill Calculator

## Description

The Flatmates Bill Calculator is a web application designed to simplify the process of splitting bills among flatmates. It allows users to calculate how much each flatmate owes for shared expenses such as electricity bills, based on the number of days each person lived in the flat and the total amount due. This tool is particularly useful for roommates and students sharing accommodation, ensuring a fair and transparent way of dividing bills. This app initially was built following the instructions of Udemy course  ["The Complete Python Course in the Professional OOP Approach"](https://www.udemy.com/course/the-python-pro-course/?referralCode=D1224FDF916B73D7E740) and then upgraded by me by adding the possibility to download the PDF right from the web app and to be able to enter any number of flatmates. 

## Features

Dynamic Flatmate Addition: Users can dynamically add the details of each flatmate, including their names and the number of days they stayed in the flat.
Bill Calculation: The application calculates the individual share of each flatmate based on the total bill amount and the proportion of days they stayed.
PDF Report Generation: After calculation, the application generates a downloadable PDF report, detailing each flatmate's name and the amount they owe.
Responsive Design: The application features a user-friendly interface that adapts to various screen sizes, ensuring a seamless experience on both desktop and mobile devices.
Technologies Used

Backend: Developed using Flask, a lightweight WSGI web application framework in Python. The backend handles routing, form processing, bill calculations, and PDF generation.
Frontend: The user interface is built with HTML, CSS, and JavaScript. It features dynamic form manipulation to handle an arbitrary number of flatmates.
PDF Generation: Utilizes the FPDF library for creating PDF reports.
Styling: Custom CSS styling for a clean and modern user interface.

## Setup and Installation

1. Clone this repo or download all these files
2. Create a PyCharm (or other IDE) project and configure a Python interpreter for the project.
3. Install the required packages by running in the terminal:
   `pip install -r requirements.txt`
4. Run _main.py_ with Python.
5. Open http://127.0.0.1:5000/ on your internet browser to see the web app.

## Future Enhancements

- Validation to ensure numerical inputs for days in the house.
- Enhanced error handling and user input feedback.
- Ability to handle additional types of shared expenses.
- Improving the style of the generated PDF file, making it more informative
