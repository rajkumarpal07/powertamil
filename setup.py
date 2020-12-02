import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="powertamil", 
    version="1.0",
    author="Rajkumar Palani",
    author_email="rajkumarpalani07@gmail.com",
    description="A Python suite of Tamil NLP tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajkumarpal07/powertamil",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)