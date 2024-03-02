from pathlib import Path
import setuptools

setuptools.setup(
    name="leilapdf",
    version="0.0.1",
    description="A Python package to convert PDFs to text",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"]),
)