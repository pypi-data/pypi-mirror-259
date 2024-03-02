from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
        name="hack4u22",
        version="0.8.0",
        packages=find_packages(),
        install_requires=[],
        author="Carlos Aguilar",
        description="Biblioteca para consultar cursos de Hack4u",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://hack4u.io",
)
