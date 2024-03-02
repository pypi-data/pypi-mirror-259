from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='PremaDjango',
    version="0.1.2",
    # use_scm_version=True,
    # setup_requires=['setuptools_scm'],
    packages=find_packages(),
    install_requires=[
        'Django',
        'setuptools_scm'
    ],
    author="Premanath",
    author_email="talamarlapremanath143@gmail.com",
    description="My Short Description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prema1432/premadjango/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
    license="MIT",
)
