from setuptools import setup, find_packages

setup(
    name="CoderOfSnake",
    version="0.1",
    packages=find_packages(),
    py_modules=['helper', 'note', 'sort'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'coderofsnake=helper:main',
        ],
    }
)