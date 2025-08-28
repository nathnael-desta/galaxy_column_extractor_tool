from setuptools import setup

setup(
    name="csv_extract",
    version="1.0",
    py_modules=["csv_extract"],
    entry_points={
        'console_scripts': [
            'csv_extract = csv_extract:main',
        ],
    },
)
