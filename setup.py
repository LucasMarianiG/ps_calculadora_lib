from setuptools import setup, find_packages

# Lendo o README.md para o PyPI
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="calculadora_mari_lib",
    version="0.1.2",
    description="Biblioteca de operações matemáticas básicas em Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lucas Mariani",
    author_email="lucas2607.gomes@gmail.com",
    url="https://github.com/LucasMarianiG/ps_calculadora_lib.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
