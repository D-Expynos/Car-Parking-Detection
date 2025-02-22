from setuptools import setup, find_packages

setup(
    name="Car-Parking-Detection",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "pandas",
        "matplotlib",
        "notebook",
        "pickle-mixin",
    ],
    author="D-Expynos",
    description="An OpenCV-based system for detecting vacant and occupied parking spaces.",
    long_description=open("docs/README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/D-Expynos/Car-Parking-Detection",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
