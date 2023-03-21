"""
Set up for mymodule
"""
from setuptools import setup

requirements = ['numpy>=1.0']

setup(
    name='mymodule',
    packages=['mymodule'],
    version=0.1,
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={'console_scripts':['sky_sim= mymodule.sky_sim:main']}
)
