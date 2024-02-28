from setuptools import setup, find_packages

setup(
    name='hyprbots_logging_framework',
    version='0.1.0',
    author='Anonymous',
    author_email='anonymous@xyz.com',
    description='A custom logging package for multiple platforms',
    packages=find_packages(),
    url='https://github.com/hyprbots/custom_logging',
    install_requires=[
        'python-logstash-async',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
