from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyspark_utility",
    version="0.4.0",
    author="Ashish Garg",
    author_email="ashishgargmp@email.com",
    description="This project is meant to help pyspark user (Databricks) to get some utility functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashishgargmp/pyspark_utils_agarg",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add your project dependencies here
        "pyspark>=3.5.0",
        "fakers>=0.42.0"
    ],
)
