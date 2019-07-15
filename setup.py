import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="pandasUtilities",
    version="0.0.2",
    license='MIT',
    author="Gaurav Shimpi",
    author_email="shimpigaurav0@gmail.com",
    description="Pandas utilities which makes your work with Pandas easy and effective.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gauravshimpi/PandasUtilities",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    download_url = 'https://github.com/gauravshimpi/PandasUtilities/archive/V_0_0_2.tar.gz',
    keywords = ['pandas', 'utilities', 'PandasUtilities'],
    install_requires=setuptools.find_packages(),
)
