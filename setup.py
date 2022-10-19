
import setuptools

setuptools.setup(
    name="householdpower",
    version="0.1.0",
    url="https://github.com/Asmaa-khorkhash/householdpower",
    author="Asmaa khorkhash",
    author_email="asmaakhorkhash@gmail.com",
    description=" Measurements of electric power consumption in one household",
    long_description=open('DESCRIPTION.rst').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    package_data={'': ['data/*.csv']},
)