from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyside6-drawer',
    version='0.0.1',
    author='Simon Wu',
    author_email='simonwu22@outlook.com',
    license='MIT',
    packages=find_packages(),
    # package_data={'pyqt_drawer.ico': ['drawer.svg']},
    description='PySide6 drawer',
    url='https://github.com/sw22m/PySide6-Drawer.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PySide6'
    ]
)