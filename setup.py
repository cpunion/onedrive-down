"""Download file from OneDrive.
"""
from setuptools import setup

setup(
    name='onedrive-down',
    version='0.1.0',
    description='Download file from OneDrive.',
    long_description=__doc__,
    author='Li Jie',
    author_email='cpunion@gmail.com',
    entry_points={
        'console_scripts': ['onedrive-down=onedrive_down:main']
    },
)
