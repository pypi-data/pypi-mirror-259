from setuptools import find_packages, setup, extension

with open("KMIS_BI/README.md", "r") as f:
    long_description = f.read()

setup(
    name="KMIS_BI",
    version="0.1.0",
    description="My own tester",
    package_dir={"": "KMIS_BI"},
    packages=find_packages(where="KMIS_BI"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/KMIS-BI/1.0.0/",
    author="marast",
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
