from setuptools import setup, find_packages

setup(
    name="samplesxsdas",  # Package name
    version="0.0.0",  # Package version
    description="parallel, efficient and ensemble analysis of Rao's Q spectral diversity using remote sensing datasets.",
    author="Mohammad Reza Fathi",
    author_email="mmadrzfathi@gmail.com",
    packages=find_packages(),  # Automatically finds packages in the directory
    install_requires=[  # List of required dependencies
        "tk",
        "ipywidgets",
        "xarray",
        "rioxarray",
        "rasterio",
        "numpy",
        "spyndex",
        "pandas",
        "matplotlib",
        "seaborn",
        "ray",
        "tqdm",
    ],
)
