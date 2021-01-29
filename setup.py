from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_data_package=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
