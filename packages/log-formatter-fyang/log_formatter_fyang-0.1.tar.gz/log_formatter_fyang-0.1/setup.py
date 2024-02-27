# setup.py

from setuptools import setup, find_packages

setup(
    name='log_formatter_fyang',
    version='0.1',
    description='log formatting utility',
    license="MIT",
    author="ocean",
    packages=find_packages(),
    long_description="A simple log formatting utility for Python projects",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='logging log formatting',
    python_requires='>=3.7',
    install_requires=[
        'requests',
        'numpy',
    ]
)

