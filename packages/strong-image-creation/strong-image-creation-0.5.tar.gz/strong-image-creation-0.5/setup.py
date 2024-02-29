from setuptools import setup, find_packages

setup(
    name="strong-image-creation",
    entry_points={
        'console_scripts': [
            'strong_image_creation = strong_image_creation.strong_image_creation:main',
        ],
    },
    version="0.5",
    packages=find_packages(),
    install_requires=[
        'imagecodecs',
        'numpy',
        'tifffile',
        'fabio',
        'pyqt5',
    ],
    author="biocat",
    author_email="xli239@hawk.iit.edu",
    description="A package to create summed images from a series of tiff or h5 files in a folder.",
    url="https://github.com/biocatiit/musclex",
)
