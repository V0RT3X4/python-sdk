import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("./vortexasdk/version.py") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="vortexasdk",
    version=version["__version__"],
    author="Vortexa Developers",
    author_email="developers@vortexa.com",
    description="Vortexa SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/vortechsa/python-sdk",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=0.25.2",
        "requests==2.22.0",
        "jsons==1.0.0",
        "flatten-dict==0.2.0",
        "tqdm==4.38.0",
    ],
    extras_require={
        "tests": [
            "jupyter==1.0.0",
            "mkdocs==1.0.4",
            "mypy==0.770",
            "pytest==5.2.4",
            "pre-commit==1.20.0",
            "flake8==3.8.4",
            "pydoc-markdown==2.0.5",
            "six==1.12.0",
            "tabulate==0.8.7",
            "xlrd==1.2.0"
        ],
        "deploy": [
            "wheel==0.36.2",
            "twine==3.3.0"
        ]
    },
)
