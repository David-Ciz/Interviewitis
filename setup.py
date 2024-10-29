from setuptools import setup, find_packages

setup(
    name="interviewitis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "termcolor",  # For colored console output
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A cheeky package to help you survive technical interviews",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/interviewitis",
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