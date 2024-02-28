from setuptools import setup, find_packages
import codecs
import os


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Setting up
setup(
    name="pasec",
    version='2.0.0',
    author="ssuroj (Suroj Sapkota)",
    author_email="<surojsapkota1@gmail.com>",
    description='A strong password Generator using weak passphrase.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['Password', 'Security', 'Password Generator', 'PaSec'],
    url='https://github.com/5uroj/pasec-py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
