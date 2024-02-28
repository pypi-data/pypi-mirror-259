from setuptools import setup, find_packages


setup(
    name='HGVStoFASTA',
    version='0.3.5',
    license='GPL-3.0',
    author="Taner Karagol",
    author_email='taner.karagol@gmail.com',
    url='https://github.com/karagol-taner/HGVS-missense-variants-to-FASTA',
    keywords='HGVS, FASTA',
    install_requires=[
          'biopython',
      ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'HGVStoFASTA = __main__:main',
        ],
    },

)