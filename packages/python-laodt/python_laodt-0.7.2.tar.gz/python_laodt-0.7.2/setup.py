from setuptools import setup, find_packages
 
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]
 
setup(
  name='python_laodt',
  version='0.7.2',
  description='Pyhon LaoDT Libary',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='barlardcuda',
  author_email='barluscuda@gmail.com',
  license='BLCD1234', 
  classifiers=classifiers,
  keywords='pythonlaodt', 
  packages=find_packages(),
  install_requires=[''] 
)