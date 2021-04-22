import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Pepfeature",
    version="1.0.0",
    description="A package that consists of functions for calculating epitope/peptide features for prediction purposes (Feature calculation/extraction)",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/essakh/pepfeature",
    author="Essa Khan",
    author_email="contact.essakh@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pepfeature"],
    include_package_data=True,
    install_requires=["pandas", "numpy"],
    # entry_points={ WHAT SHOULD RUN WHENEVER THE PACKAGE IS EXECUTED AS: python -m pepfeature
    #     "console_scripts": [
    #         "realpython=reader.__main__:main",
    #     ]
    # },
)