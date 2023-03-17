import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "not-in-pandas",
    version = "0.1.1",
    author = "lucas-abbate",
    author_email = "abbatelucas@gmail.com",
    description = "A package that adds the notin method to pandas.Series and pandas.DataFrame objects",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/lucas-abbate/not-in-pandas",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages = ['not_in_pandas'],
    python_requires = ">=3.6",
    install_requires = ['pandas>=1.0.0']
)