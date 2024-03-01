# setup.py
from setuptools import setup, find_packages

setup(
    name='lilzey_generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
         'cann_calculator==1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'lilzey-generator=lilzey_generator.main:main',
        ],
    },
    author='lilzey',
    author_email='lilzey0101@gmail.com',
    bugtrack_url='https://github.com/hw010101/lilzey_generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    project_urls={
        'Source': 'https://github.com/hw010101/lilzey_generator',
    },
)
