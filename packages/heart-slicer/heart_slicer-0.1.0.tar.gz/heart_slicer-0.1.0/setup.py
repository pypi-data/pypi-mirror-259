from setuptools import setup, find_packages

setup(
    name="heart_slicer",
    version="0.1.0",
    description=
    """A package containing scripts to process images of slices of a heart that are colored with ... and preprocessed to simplify the colors. See paper xxxx for more information on the process.""",
    author="True Galaxus",
    author_email="ron.reclame@gmail.com",
    packages=find_packages(),
    install_requires=["numpy", "pillow", "pyyaml", "matplotlib"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    include_package_data=True,
    # files to include are defined in MANIFEST.in
)