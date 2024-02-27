from setuptools import find_packages, setup

setup(
    name='milea-base',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,  # Schließt Dateien ein, die in MANIFEST.in aufgeführt sind
    install_requires=[
        'Django>=5.0',
    ],
    author='red-pepper-services',
    author_email='pypi@schiegg.at',
    description='Milea Framework - Base Module',
    license='MIT',
)
