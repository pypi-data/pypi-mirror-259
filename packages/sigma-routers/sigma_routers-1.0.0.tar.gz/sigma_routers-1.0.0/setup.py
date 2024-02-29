from setuptools import setup, find_packages

setup(
    name='sigma_routers',
    version='1.0.0',
    author='Boris Ranchev',
    author_email='ranchev.boris@abv.com',
    description='Endpoints Access Router Package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests',
    ],
)
