
from setuptools import find_packages, setup

setup(
    name='milea-base',
    version='0.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django>=5.0'],
    author='red-pepper-services',
    author_email='pypi@schiegg.at',
    description='Milea Framework - Milea Base Module',
    license='MIT',
)
