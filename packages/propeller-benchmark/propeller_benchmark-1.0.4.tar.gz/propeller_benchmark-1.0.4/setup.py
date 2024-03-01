import setuptools

setuptools.setup(
    name="propeller_benchmark", 
    version="1.0.4",
    author="Gabriele Ruini",
    author_email="g.ruini@shadowycreators.com",
    description="Tool to compare dexes performances",
    long_description="Tool to compare dexes performances",
    packages=setuptools.find_packages(),
    install_requires=[
        "python-dotenv",
        "requests",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
