from setuptools import find_namespace_packages, setup

setup(
    name='clean',
    version='1.0.0',
    description='clean code',
    author='Tetiana',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': ['clean-folder = clean_folder.clean:main']
    }
)
