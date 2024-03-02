from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='superpandas',
    version='0.1.0',    
    description='SuperPandas is a Python library that turbocharges Pandas DataFrames with the power of Generative AI.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MaveriQ/superpandas',
    author='Haris Jabbar',
    author_email='harisjabbar@gmail.com',
    license='Apache-2.0 license',
    package_data={'': ['*.json', '*.txt', '*.pkl']},
    include_package_data=True,  
    install_requires=['transformers>=4.5.0',
                      'regex',
                      'pandas',
                      'vllm'                     
                      ],
    python_requires=">=3.7.0",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)