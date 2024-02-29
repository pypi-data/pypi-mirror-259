from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='dbaae',
    version='0.0.6',
    description='Adversarial Autoencoder with dynamic batching package',
    author='kyung dae ko',
    author_email='gogoaja70@hotmail.com',
    url='https://github.com/LMSCGR/DB-AAE',
    install_requires=required,
    packages=find_packages(),
    #packages=['aae'],
    #package_dir={"": "."},
    #package_data={"data": ["*.h5ad"]},
    entry_points={
        'console_scripts': [
            'dbaae= dbaae.__main__:main'
    ]},
    license='Apache License 2.0',
    keywords=['DB-AAE', 'Adversarial Autoencoder', 'python single cell', 'scRNA-seq', 'pypi'],
    python_requires='>=3.8',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
)
