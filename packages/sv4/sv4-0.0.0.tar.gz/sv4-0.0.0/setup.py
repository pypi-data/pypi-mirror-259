from setuptools import setup


setup(
    name="sv4",
    version="0.0.0",
    author="André Bienemann",
    author_email="andre.bienemann@gmail.com",
    extras_require={
        "dev": [
            "black",
            "coverage",
            "isort",
            "twine",
            "wheel",
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
