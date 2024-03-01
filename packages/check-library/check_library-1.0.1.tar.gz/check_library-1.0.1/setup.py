from setuptools import setup

setup(
    name='check_library',
    version='1.0.1',
    py_modules=['check_library'],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'check_library=check_library:main',
        ],
    },
)
