import os
import shutil

import click


@click.command()
@click.option("-f", "--filename", type=str)
def encrypt(filename):
    def _create_setup(filename, exclude_list: list = []):
        str = '''
from distutils.core import setup
from Cython.Build import cythonize
exclude_list = {}
if __name__ == '__main__':
    setup(ext_modules = cythonize(r'{}', exclude=exclude_list, language_level=3))'''.format(
            exclude_list, filename)
        with open('_setup.py', "w") as file:
            file.write(str)

    _create_setup(filename)
    os.system("python _setup.py build_ext --inplace")
    shutil.rmtree("build")
    os.remove("_setup.py")
    os.remove(filename.replace(".py", ".c"))
