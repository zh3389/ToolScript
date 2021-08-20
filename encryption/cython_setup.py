from distutils.core import setup
from Cython.Build import cythonize

setup(name='Hello app',
      ext_modules=cythonize('main.py'))