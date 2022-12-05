from setuptools import setup

setup(
    name="dacite2",
    version="2.0b2",
    description="Simple creation of data classes from dictionaries (fork of dacite).",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Konrad Hałas",
    author_email="halas.konrad@gmail.com",
    maintainer="Idan Miara",
    maintainer_email="idan@miara.com",
    url="https://github.com/idanmiara/dacite",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    keywords="dataclasses",
    packages=["dacite"],
    package_data={"dacite": ["py.typed"]},
    extras_require={
        "dev": [
            "pytest>=5",
            "pytest-cov",
            "coveralls",
            "black",
            "mypy",
            "pylint",
            "numpy>=1.21.0",
        ]
    },
)
