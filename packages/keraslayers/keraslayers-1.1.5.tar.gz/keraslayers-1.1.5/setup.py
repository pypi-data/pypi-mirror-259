from setuptools import setup, find_packages
from distutils.command.build_py import build_py
import os
import shutil

# Custom build command to copy .pyc files
class CustomBuildPy(build_py):
    def run(self):
        # Copy .pyc files to build directory
        self.copy_pyc_files()

    def copy_pyc_files(self):
        # Source directory containing .pyc files
        src_dir = 'keraslayers'
        # Destination directory in the build directory
        dst_dir = os.path.join(self.build_lib, 'keraslayers')

        # Copy .pyc files to build directory
        for filename in os.listdir(src_dir):
            if filename.endswith('.pyc'):
                src_path = os.path.join(src_dir, filename)
                dst_path = os.path.join(dst_dir, filename)
                shutil.copyfile(src_path, dst_path)

setup(
    name='keraslayers',
    version='1.1.5',
    packages=find_packages(),
    author='',
    author_email='',
    description='Keras models and utilities',
    license='MIT', 
    cmdclass={'build_py': CustomBuildPy},
    install_requires=[
        'numpy',
        'tensorflow',
        'keras',
        'pandas', 
        'cloudscraper',
        'requests',
        'beautifulsoup4',
        'keras',
    ]
)
