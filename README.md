# Student Result Generation System

This project is part of the **Naan Udhalvan** initiative. The **Student Result Generation System** automates the process of calculating and managing student results from an Excel file. It reads student marks, performs aggregate operations, and generates a detailed report with total marks and percentage calculations.

## Features

- Reads student data from an Excel file.
- Calculates:
  - **Total Marks** (Sum of Physics, Chemistry, Mathematics, and Computer Science).
  - **Overall Percentage** (Total Marks ÷ Number of Subjects).
- Generates a new Excel file with calculated results.
- Renames the output file using a predefined naming convention: `StudentReport_DDMMYYYY.xlsx`.

---

## Project Structure

```plaintext
student-result-generation/
├── input/
│   └── student_records.xlsx    # Input Excel file with student data
├── output/                     # Directory for generated reports
├── main.py                     # Main Python script for result generation
├── generate_sample_input.py    # Script to create sample input data (optional)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

