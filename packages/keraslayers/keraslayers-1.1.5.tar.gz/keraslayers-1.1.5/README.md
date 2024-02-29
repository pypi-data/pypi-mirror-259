from setuptools import setup, find_packages

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
