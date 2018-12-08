""" Setup for python-panasonic-comfort-cloud """

from setuptools import setup

setup(
    name='pcomfortcloud',
    version='0.0.11',
    description='Read and change status of Panasonic Comfort Cloud devices',
    long_description='A python module for reading and changing status of panasonic climate devices through Panasonic Comfort Cloud app api',
    url='http://github.com/lostfields/python-panasonic-comfort-cloud',
    author='Lostfields',
    license='MIT',
    classifiers=[
       'Topic :: Home Automation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='home automation panasonic climate',
    install_requires=['requests>=2.20.0'],
    packages=['pcomfortcloud'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'pcomfortcloud=pcomfortcloud.__main__:main',
        ]
    })