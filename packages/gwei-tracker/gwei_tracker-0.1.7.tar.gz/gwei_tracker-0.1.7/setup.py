from setuptools import setup, find_packages


setup(
    name="gwei_tracker",
    version="0.1.7",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["playwright==1.41.2","etherscan-python==2.1.0","pyee==11.0.1"],
)