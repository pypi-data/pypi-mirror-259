from setuptools import find_packages, setup, extension

with open("bikmis/README.md", "r") as f:
    long_description = f.read()

setup(
    name="kmis",
    version="0.2.4",
    description="My own tester",
    package_dir={"": "bikmis"},
    packages=find_packages(where="bikmis"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Marast",
    author_email="havlicek.mara@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
