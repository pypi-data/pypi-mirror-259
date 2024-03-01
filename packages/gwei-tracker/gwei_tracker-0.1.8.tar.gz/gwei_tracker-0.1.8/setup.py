from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    description = fh.read()

setup(
    name="gwei_tracker",
    version="0.1.8",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["playwright==1.41.2","etherscan-python==2.1.0","pyee==11.0.1"],
    long_description=description,
    long_description_content_type="text/markdown",
)