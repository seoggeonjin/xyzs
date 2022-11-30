import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mcal",
    version="0.0.2",
    author="seoggeonjins",
    author_email="seoggeonjin@gmail.com",
    description="A small equation solve program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seoggeonjin/xxyz",
    download_url="https://github.com/seoggeonjin/xyzs/archive/master.zip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
