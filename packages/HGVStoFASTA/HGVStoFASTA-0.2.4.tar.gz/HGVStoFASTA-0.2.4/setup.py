from setuptools import setup, find_packages


setup(
    name='HGVStoFASTA',
    version='0.2.4',
    license='GPL-3.0',
    author="Taner Karagol",
    author_email='taner.karagol@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/karagol-taner/HGVS-missense-variants-to-FASTA',
    keywords='HGVS, FASTA',
    install_requires=[
          'biopython',
      ],
    entry_points={
        'console_scripts': [
            'HGVStoFASTA = HGVStoFASTA.scr.HGVStoFASTA:main',
      ],
    },

)