from setuptools import setup, find_packages

setup(
    name='github-recover',
    version='01',
    author='amirali irvany',
    author_email='dev.amirali.irvany@gmail.com',
    description='A small GitHub REST API client written in Python ',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/metect',
    install_requires=['requests'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
