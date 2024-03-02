from setuptools import setup, find_packages
setup(
    name='pipmin',
    version='0.0.2',
    author='Harshit Sharma',
    author_email='harshit158@gmail.com',
    description='Package to generate trimmed requirements.txt',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pipmin=pipmin.trim:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
    python_requires='>=3.9.0',
    install_requires=[
        'pipdeptree==2.15.1',
    ]
)