try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pymarc2jsonl',
      version='0.0.1',
      description='MARC21 to MarcXchange formatted ld-JSON and reverse converter based on pymarc',
      url='https://github.com/slub/pymarc2jsonl',
      author='Bernhard Hering',
      author_email='bernhard.hering@slub-dresden.de',
      license="Apache 2.0",
      packages=[
          'marc2jsonl',
          'json2marc21',
          'json2marcxml'
          ],
      package_dir={
          'marc2jsonl': 'marc2jsonl',
          'json2marc21': 'json2marc21',
          'json2marcxml': 'json2marc21'
          },
      install_requires=[
          'argparse>=1.4.0',
          'pymarc>=4.0.0',
          'six>=1.14.0',
          'es2json>=0.0.1'
      ],
      python_requires=">=3.6.*",
      entry_points={
          "console_scripts": [
              "pymarc2jsonl=marc2jsonl.marc2jsonl:main",
              "json2marc21=json2marc21.json2marc21:main",
              "json2marcxml=json2marc21.json2marcxml:main"
              ]
          }
      )
