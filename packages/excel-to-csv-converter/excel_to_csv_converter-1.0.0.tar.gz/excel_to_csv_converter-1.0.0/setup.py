from setuptools import setup, find_packages

setup(
    name='excel_to_csv_converter',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'openpyxl',
    ],
    entry_points={
        'console_scripts': [
            'excel-to-csv=package.converter:main',
        ],
    },
    python_requires='>=3.6',
    author='Omar Morrison',
    author_email='morrisonomar@yahoo.com',
    description='Convert Excel files to CSV format',
    url='https://github.com/sportyomar/automation_tools',
)
