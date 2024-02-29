from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
    name="cyp2d6_parser",
    version="2.0.1",
    description="Parser to match CYP2D6 parsing reccomendations by PharmVar.",
    author="Andrew Haddad, PharmD",
    author_email="andrew.haddad@pitt.edu",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["cyp2d6_parser = cyp2d6_parser.__main__:main"]},
    install_requires=["pandas", "numpy"],
    package_data={"cyp2d6_parser": ["*.csv"]},
    include_package_data=True,
)
