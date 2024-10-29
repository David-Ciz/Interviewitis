# setup.py
from setuptools import setup, find_packages
from pathlib import Path

# Read README with proper encoding
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="interviewitis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "termcolor",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A cheeky package to help you survive technical interviews",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/David-Ciz/Interviewitis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Software Development",
    ],
    python_requires=">=3.6",
)
