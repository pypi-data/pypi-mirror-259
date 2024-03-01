from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='tensor_library',
  version='0.0.1',
  author='DexTeam',
  author_email='bankcommandoofficial@gmail.com',
  description='It is a simple library for the Python programming language. It will be updated frequently.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/andrekornyk/Library-for-Python-by-DexTeam?tab=readme-ov-file',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'https://github.com/andrekornyk/Library-for-Python-by-DexTeam?tab=readme-ov-file'
  },
  python_requires='>=3.8'
)