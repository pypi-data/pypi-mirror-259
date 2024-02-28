from setuptools import setup, find_packages

setup(
    name='cs1-graphics',
    version='1.1',
    packages=find_packages(),
    install_requires=['pygame'],
    author='Jack Seigerman',
    author_email='jacks3ds@gmail.com',
    description='A simple Python graphics library',
    long_description_content_type='text/markdown',
    url='https://github.com/jackSeigerman/cs1-graphics',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
