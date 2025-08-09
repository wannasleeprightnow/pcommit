from setuptools import setup

setup(
    name='pcommit',
    version='1.0',
    py_modules=['pcommit'],
    entry_points={
        'console_scripts': [
            'pcommit=pcommit:main',
        ],
    },
)