from setuptools import setup, find_packages

setup(
    name='twosum',
    version='0.2.0',  # Update the version number
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'twosum = twosum.twosum:main',
        ],
    },
    install_requires=[
        'requests>=2.0.0',
        'numpy>=1.0.0',
    ],
)

