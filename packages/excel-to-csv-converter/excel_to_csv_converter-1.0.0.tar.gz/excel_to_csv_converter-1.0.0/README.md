# Excel to CSV Converter

The Excel to CSV Converter is a Python script that allows you to convert Excel files (.xlsx) into CSV (Comma-Separated Values) format. It provides a graphical user interface (GUI) built with Tkinter for easy file selection and conversion.

## Features
- Convert multiple Excel files into CSV format simultaneously.
- Graphical user interface (GUI) for intuitive operation.
- Displays sheet names of loaded Excel files.
- Handles error cases gracefully with informative error messages.

## Dependencies
- Python 3.x
- openpyxl (Python library for reading and writing Excel files)

## Installation
1. Make sure you have Python 3.x installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).
2. Install the required Python library using pip:
   ```bash
   pip install openpyxl

# Usage
1. Clone the repository or download the source code.
2. Navigate to the project directory in your terminal.
3. Run the script using Python:
   
```bash
python excel_to_csv_converter.py
```
4. Click on "Load XLSX Files" to select one or more Excel files (.xlsx) you want to convert.
5. Click on "Select Output Directory" to choose the directory where you want to save the converted CSV files.
6. Click on "Convert to CSV" to start the conversion process.
7. Once the conversion is complete, the script will display the number of CSV files generated.

# Examples

```python
# Example usage of the ExcelToCsvConverter class

import tkinter as tk
from excel_to_csv_converter import ExcelToCsvConverter

root = tk.Tk()
app = ExcelToCsvConverter(root)
root.mainloop()
```

# How to Contribute

Contributions to improve Excel to CSV Converter are welcome! Here's how you can contribute:

* Fork the repository.
* Make your changes and enhancements.
* Submit a pull request with a clear description of your changes.

# License

This project is licensed under the MIT License.


