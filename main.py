import pandas as pd
from datetime import datetime
import os

# Step 1: Define file paths
input_file = "input/student_records.xlsx"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

# Step 2: Read the Excel file
try:
    df = pd.read_excel(input_file)

    # Step 3: Perform calculations
    df['Total'] = df[['Physics', 'Chemistry', 'Mathematics', 'ComputerScience']].sum(axis=1)
    df['OverallPercentage'] = (df['Total'] / 4).round(2)

    # Step 4: Save the new Excel file
    output_file = os.path.join(output_dir, "StudentReport.xlsx")
    df.to_excel(output_file, index=False)

    # Step 5: Rename the file with the naming convention
    current_date = datetime.now().strftime("%d%m%Y")
    renamed_file = os.path.join(output_dir, f"StudentReport_{current_date}.xlsx")
    os.rename(output_file, renamed_file)

    print(f"File saved and renamed successfully as {renamed_file}")
except Exception as e:
    print(f"An error occurred: {e}")
