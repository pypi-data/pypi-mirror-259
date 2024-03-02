from setuptools import setup, find_packages

setup(
    name="PaRaVis",  # Package name
    version="1.0.0",  # Package version
    description="parallel, efficient and ensemble analysis of Rao's Q spectral diversity using remote sensing datasets.",
    author="Mohammad Reza Fathi",
    author_email="mmadrzfathi@gmail.com",
    packages=find_packages(),  # Automatically finds packages in the directory
    install_requires=[  # List of required dependencies
        "tkinter",
        "python3-tk",  # Ubuntu package for tkinter support
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
